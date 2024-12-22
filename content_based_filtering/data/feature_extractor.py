import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from scipy.sparse import csr_matrix, hstack
from content_based_filtering.src.dependencies import IFeatureExtractor


class TrackFeatureExtractor(IFeatureExtractor):
    def __init__(self):
        self.numeric_columns = [
            "danceability",
            "energy",
            "tempo",
            "acousticness",
            "valence",
            "key",
            "mode",
        ]
        self.tfidf = TfidfVectorizer(max_features=10000, stop_words="english")
        self.scaler = MinMaxScaler()

    def extract_features(self, df: pd.DataFrame) -> csr_matrix:
        genre_features = self.tfidf.fit_transform(df["track_genre"])
        normalized_numeric = self.scaler.fit_transform(df[self.numeric_columns])
        combined_features = hstack(
            [csr_matrix(genre_features), csr_matrix(normalized_numeric)]
        )
        return combined_features
