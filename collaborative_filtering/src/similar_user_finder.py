from sklearn.neighbors import NearestNeighbors


class SimilarUserFinder:
    def __init__(self, n_neighbors=6):
        self.n_neighbors = n_neighbors
        self.model = None

    def train(self, sparse_matrix):
        """train the nearest neighbors model on the sparse matrix"""
        self.model = NearestNeighbors(
            metric="cosine", algorithm="brute", n_neighbors=self.n_neighbors, n_jobs=-1
        )
        self.model.fit(sparse_matrix)

    def find_similar_users(self, sparse_matrix, target_user_idx):
        distances, indices = self.model.kneighbors(
            sparse_matrix[target_user_idx], n_neighbors=self.n_neighbors
        )
        return indices[0][1:]  # exclude the target user itself
