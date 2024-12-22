from abc import ABC, abstractmethod
import pandas as pd
from scipy.sparse import csr_matrix


class IDataLoader(ABC):
    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        pass


class IFeatureExtractor(ABC):
    @abstractmethod
    def extract_features(self, df: pd.DataFrame) -> csr_matrix:
        pass


class ISimilaritySearch(ABC):
    @abstractmethod
    def find_similar_tracks(self, track_id: str, k: int) -> pd.DataFrame:
        pass
