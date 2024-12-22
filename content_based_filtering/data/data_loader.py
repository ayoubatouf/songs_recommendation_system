import pandas as pd
from content_based_filtering.src.dependencies import IDataLoader


class CSVDataLoader(IDataLoader):
    def __init__(self, file_path, dtype={"track_id": "category"}):
        self.file_path = file_path
        self.dtype = dtype

    def load_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.file_path, dtype=self.dtype)
        return df.drop_duplicates(subset=["track_id"], keep="first")
