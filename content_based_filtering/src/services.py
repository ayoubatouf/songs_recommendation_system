import pandas as pd
from content_based_filtering.src.dependencies import ISimilaritySearch


class RecommendationService:
    def __init__(self, df_original: pd.DataFrame, similarity_search: ISimilaritySearch):
        self.df_original = df_original  # dataset (preserved)
        self.similarity_search = similarity_search

    def recommend_for_user(self, user_id: int, k: int = 6) -> pd.DataFrame:
        user_data = self.df_original[self.df_original["userID"] == user_id]
        if user_data.empty:
            raise ValueError(f"no data found for user {user_id}")

        highest_rated_track = user_data.loc[user_data["rating"].idxmax()]
        highest_rated_track_id = highest_rated_track["track_id"]

        return self.similarity_search.find_similar_tracks(highest_rated_track_id, k)
