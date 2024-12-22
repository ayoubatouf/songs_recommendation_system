import pandas as pd
import numpy as np
from collaborative_filtering.config.paths import *


def prepare_data(df1_path, df2_path, output_path):

    df1 = pd.read_csv(df1_path, usecols=lambda column: column != "Unnamed: 0")

    df1 = df1[
        [
            "track_id",
            "track_genre",
            "danceability",
            "energy",
            "tempo",
            "acousticness",
            "valence",
            "key",
            "mode",
        ]
    ]

    df1 = df1.dropna()

    df2 = pd.read_csv(df2_path)
    df2.columns = df2.columns.str.replace("'", "").str.strip()
    df2 = df2[["userID", "rating"]]

    df2 = df2.dropna(subset=["userID"])

    df2["rating"].fillna(0, inplace=True)

    df1 = df1.dropna()

    random_indices = np.random.randint(0, len(df1), size=len(df2))

    df1_sample = df1.iloc[random_indices].reset_index(drop=True)

    df2.reset_index(drop=True, inplace=True)

    combined_df = pd.concat([df2, df1_sample], axis=1)
    combined_df.drop_duplicates(inplace=True)
    combined_df.to_csv(output_path, index=False)

    print(f"combined DataFrame shape : {combined_df.shape}")


if __name__ == "__main__":
    prepare_data(
        df1_path=SPOTIFY_DATASET_PATH,
        df2_path=SONGS_DATASET_PATH,
        output_path=USERS_TRACKS_DATASET_PATH,
    )
