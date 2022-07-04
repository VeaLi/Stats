import numpy as np
import pandas as pd
from scipy import linalg


class SSA:

    def __init__(self, window_length, step=1, n_keep=7):
        """
        Singular spectrum analysis, 
        aid in the decomposition of time series into a sum of components.

        Uses memory intensive SVD calculations, break large time series in chunks before appling.


        Parameters
        ----------
        window_length: Int
            [a]
        step: Int, default=1
            [b]
        n_keep: Int, default=7
            [c]

        Example
        ----------
        -

        References
        ----------
        1. https://www.kaggle.com/code/jdarcy/introducing-ssa-for-time-series-decomposition/notebook.
        2. https://www.wikiwand.com/en/Singular_spectrum_analysis.

        """
        self.window_length = window_length
        self.step = step
        self.n_keep = n_keep

    def transform(self, data):
        self.data_size = len(data)
        self.num_windows = int(
            (self.data_size - self.window_length + 1) / self.step)

        self.data = data
        self.get_trajectory_matrix()
        self.decompose_trajectory_matrix()
        self.build_elementary_matrices()
        self.average_elementary_matrices()

        reconstructed_signal = self.reconstruct()

        return reconstructed_signal

    def get_trajectory_matrix(self):
        self.trajectory_matrix = np.zeros(
            (self.window_length, self.num_windows))
        for j in range(0, self.num_windows, self.step):
            self.trajectory_matrix[:, j] = self.data[j: j + self.window_length]

    def decompose_trajectory_matrix(self):
        self.U, self.sigma, self.VT = linalg.svd(self.trajectory_matrix)
        self.d = np.linalg.matrix_rank(self.trajectory_matrix)

    def build_elementary_matrices(self):
        # Construct and save all the elementary matrices
        self.elementary_matrices = []

        for i in range(self.d):
            elementary_matrix = self.sigma[i] * np.outer(self.U[:, i], self.VT[i, :])
            self.elementary_matrices.append(elementary_matrix)

    def average_elementary_matrices(self):
        # Diagonally average the elementary matrices, store them as columns in array.
        self.decomposition = np.zeros((self.data_size // self.step, self.d))

        for i in range(self.d):
            reversed_elementary_matrix = self.elementary_matrices[i][::-1]
            component = []
            for j in range(-reversed_elementary_matrix.shape[0] + 1, reversed_elementary_matrix.shape[1]):
                component.append(reversed_elementary_matrix.diagonal(j).mean())

            self.decomposition[:, i] = component[:self.data_size // self.step]

    def reconstruct(self):
        # Reconstructs the time series from components, using N top components

        reconstructed_signal = self.decomposition[:, :self.n_keep].sum(axis=1).squeeze().tolist()
        return reconstructed_signal
