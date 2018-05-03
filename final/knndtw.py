from dtw import dtw
import numpy as np


class KNN_DTW(object):

	def __init__(self, n_components=1):
		self.n_components = n_components
		self.X = None
		self.y = None

	def fit(self, X, y):
		self.X = X
		self.y = y

	def _dist_matrix(self, x1, d=lambda x,y: (x-y)**2):
		dist_mat = np.empty((x1.shape[0], self.X.shape[0]))
		for i, arr_i in enumerate(x1):
			for j, arr_j in enumerate(self.X):
				dist_mat[i,j] = dtw(arr_i, arr_j, d)[0]
		return dist_mat


	def predict(self, X):
		dist_mat = self._dist_matrix(X)

		return np.take(self.y, np.argmin(dist_mat, axis=1))