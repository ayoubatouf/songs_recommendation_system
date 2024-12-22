class SongRecommender:
    @staticmethod
    def recommend_songs_for_user(
        data,
        sparse_matrix,
        user_to_index,
        song_mapping,
        target_user_id,
        similar_user_finder,
    ):
        target_user_idx = user_to_index.get(target_user_id)
        if target_user_idx is None:
            print(f"user ID {target_user_id} not found.")
            return []

        similar_users = similar_user_finder.find_similar_users(
            sparse_matrix, target_user_idx
        )

        recommended_songs = SongRecommender.get_top_rated_songs_from_similar_users(
            data, similar_users
        )

        print(
            f"\nrecommended songs for user {target_user_id} based on similar users' highest-rated songs:"
        )
        for i, song_id in enumerate(recommended_songs):
            song_name = song_mapping.get(song_id, song_id)
            print(f"recommendation {i + 1}: {song_name}")

        return recommended_songs

    @staticmethod
    def get_top_rated_songs_from_similar_users(data, similar_users):
        recommended_songs = []
        for user_idx in similar_users:
            user_ratings = data[data["userID"] == user_idx]
            highest_rated_song = user_ratings[
                user_ratings["rating"] == user_ratings["rating"].max()
            ]

            if not highest_rated_song.empty:
                most_rated_song_id = highest_rated_song["songID"].iloc[0]
                recommended_songs.append(most_rated_song_id)

        # remove duplicates
        return list(set(recommended_songs))

    @staticmethod
    def print_user_songs(data, similar_users, song_mapping):
        for user_idx in similar_users:
            user_ratings = data[data["userID"] == user_idx]
            print(f"\nsongs and ratings for similar user {user_idx}:")
            for index, row in user_ratings.iterrows():
                song_name = song_mapping.get(row["songID"], row["songID"])
                print(f"song: {song_name}, rating: {row['rating']}")
