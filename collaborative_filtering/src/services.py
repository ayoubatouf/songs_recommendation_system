import os
from fastapi import HTTPException
from collaborative_filtering.config.paths import SONGS_DATASET_PATH
from collaborative_filtering.data.data_loader import DataLoader
from collaborative_filtering.src.similar_user_finder import SimilarUserFinder
from collaborative_filtering.src.song_recommender import SongRecommender
from collaborative_filtering.src.sparse_matrix_builder import SparseMatrixBuilder


class ResourceManager:
    """manages resources to avoid redundant computations"""

    def __init__(self):
        self.data = None
        self.user_to_index = None
        self.song_to_index = None
        self.sparse_matrix = None
        self.similar_user_finder = None
        self.song_mapping = None

    def initialize_resources(self):
        if self.data is None:
            file_path = SONGS_DATASET_PATH
            if not os.path.exists(file_path):
                raise HTTPException(status_code=400, detail="file not found.")

            self.data = DataLoader.load_data(file_path)

            (
                self.user_to_index,
                self.song_to_index,
                user_ids,
                song_ids,
            ) = DataLoader.create_user_song_mappings(self.data)

            self.sparse_matrix = SparseMatrixBuilder.build_sparse_matrix(
                self.data, self.user_to_index, self.song_to_index
            )

            self.similar_user_finder = SimilarUserFinder(n_neighbors=6)
            self.similar_user_finder.train(self.sparse_matrix)

            self.song_mapping = dict(
                zip(self.data["songID"].unique(), self.data["songID"].unique())
            )

    def get_resources(self):
        if self.data is None:
            self.initialize_resources()
        return (
            self.data,
            self.user_to_index,
            self.song_to_index,
            self.sparse_matrix,
            self.similar_user_finder,
            self.song_mapping,
        )


resource_manager = ResourceManager()


def recommend_songs(target_user_id: int):
    (
        data,
        user_to_index,
        song_to_index,
        sparse_matrix,
        similar_user_finder,
        song_mapping,
    ) = resource_manager.get_resources()

    return SongRecommender.recommend_songs_for_user(
        data,
        sparse_matrix,
        user_to_index,
        song_mapping,
        target_user_id,
        similar_user_finder,
    )
