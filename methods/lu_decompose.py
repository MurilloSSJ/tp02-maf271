from scipy.linalg import lu_factor, lu_solve
from methods.abstract_resolver import AbstractResolver

class LuDecompose(AbstractResolver):
    def _solve(self, A, b):
        LU, piv = lu_factor(A)
        x = lu_solve((LU, piv), b)
        return x