import pandas as pd


class DataLoader:
    @staticmethod
    def load_data(file_path):
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.replace("'", "").str.strip()
        return data

    @staticmethod
    def create_user_song_mappings(data):
        """create mappings for user and song IDs to matrix indices"""
        user_ids = data["userID"].unique()
        song_ids = data["songID"].unique()
        user_to_index = {user: idx for idx, user in enumerate(user_ids)}
        song_to_index = {song: idx for idx, song in enumerate(song_ids)}
        return user_to_index, song_to_index, user_ids, song_ids
