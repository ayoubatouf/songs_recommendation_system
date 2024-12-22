from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

SONGS_DATASET_PATH = PROJECT_ROOT / "data" / "songsDataset.csv"
SPOTIFY_DATASET_PATH = PROJECT_ROOT / "data" / "spotify_dataset.csv"
USERS_TRACKS_DATASET_PATH = PROJECT_ROOT / "data" / "users_tracks_dataset.csv"
