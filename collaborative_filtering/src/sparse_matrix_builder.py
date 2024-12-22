import scipy.sparse as sp


class SparseMatrixBuilder:
    @staticmethod
    def build_sparse_matrix(data, user_to_index, song_to_index):
        rows = data["userID"].map(user_to_index)
        cols = data["songID"].map(song_to_index)
        ratings = data["rating"]
        sparse_matrix = sp.csr_matrix(
            (ratings, (rows, cols)), shape=(len(user_to_index), len(song_to_index))
        )
        return sparse_matrix
