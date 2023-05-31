from methods.abstract_resolver import AbstractResolver
import numpy as np

class Jacobi(AbstractResolver):
    def _solve(self, A, b, max_iterations=100, tolerance=1e-6):
        n = len(A)
        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)
        x0 = self.get_xo(A)
        x = np.array(x0, dtype=float)
        x_prev = np.array(x0, dtype=float)
        iterations = 0

        while iterations < max_iterations:
            for i in range(n):
                sum_term = 0.0
                for j in range(n):
                    if j != i:
                        sum_term += A[i, j] * x_prev[j]
                x[i] = (b[i] - sum_term) / A[i, i]

            if np.linalg.norm(x - x_prev) < tolerance:
                break

            x_prev = np.array(x, dtype=float)
            iterations += 1

        return x
    
    def get_xo(self, A):
        n = len(A)
        x0 = np.ones(n)  # vetor inicializado com valores 1
        
        for i in range(n):
            row_sum = np.sum(np.abs(A[i]))  # soma dos valores absolutos da linha i
            x0[i] = row_sum / np.abs(A[i, i])  # média da linha i dividida pelo elemento diagonal
            
        return x0