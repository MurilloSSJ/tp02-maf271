from methods.abstract_resolver import AbstractResolver
import numpy as np

class GaussSeidSolver(AbstractResolver):
    def _solve(self, A, b, tolerance=1e-6):
        n = len(A)
        x = np.zeros(n)

        while(True):
            x_new = np.zeros(n)

            for i in range(n):
                sum_term = 0
                for j in range(n):
                    if j != i:
                        sum_term += A[i][j] * x_new[j]

                x_new[i] = (b[i] - sum_term) / A[i][i]

            if np.linalg.norm(x_new - x) < tolerance:
                break

            x = x_new

        return x