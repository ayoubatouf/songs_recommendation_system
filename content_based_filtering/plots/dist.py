import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collaborative_filtering.config.paths import USERS_TRACKS_DATASET_PATH


def plot_numerical_distributions(df: pd.DataFrame, numerical_columns: list):

    plt.figure(figsize=(15, 10))

    for i, column in enumerate(numerical_columns, 1):
        plt.subplot(3, 3, i)
        sns.histplot(df[column], kde=True, bins=10, color="skyblue", edgecolor="black")
        plt.title(f"distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("frequency")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":

    df = pd.read_csv(USERS_TRACKS_DATASET_PATH)
    numerical_columns = [
        "danceability",
        "energy",
        "tempo",
        "acousticness",
        "valence",
        "key",
        "mode",
    ]
    plot_numerical_distributions(df, numerical_columns)
