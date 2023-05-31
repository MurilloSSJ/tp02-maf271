from methods.abstract_resolver import AbstractResolver
from scipy.linalg import cholesky, solve_triangular
from numpy.linalg import LinAlgError


class CholeskyDecomposer(AbstractResolver):
    def _solve(self, A, b):
        try:
            L = cholesky(A)
        except LinAlgError:
            print('Matrix is not positive definite')
            return [0 for _ in range(len(A))]
        y = solve_triangular(L, b, lower=True)
        x = solve_triangular(L.T, y)
        return x