import numpy as np
import faiss
import pandas as pd
from scipy.sparse import csr_matrix
from content_based_filtering.src.dependencies import ISimilaritySearch


class FaissSimilaritySearch(ISimilaritySearch):
    def __init__(self, df: pd.DataFrame, features: csr_matrix):
        self.df = df
        self.features = np.float32(features.toarray())  # FAISS requires dense features
        self.index = faiss.IndexFlatL2(self.features.shape[1])
        self.index.add(self.features)

    def find_similar_tracks(self, track_id: str, k: int) -> pd.DataFrame:
        track_index = self.df[self.df["track_id"] == track_id].index[0]
        distances, indices = self.index.search(
            self.features[track_index : track_index + 1], k
        )
        similar_tracks = self.df.iloc[indices[0]].copy()
        similar_tracks["similarity_score"] = distances[0]
        return similar_tracks[similar_tracks["track_id"] != track_id]
