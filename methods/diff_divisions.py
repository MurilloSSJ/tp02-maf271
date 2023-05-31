from methods.interpolate_abstract import AbstractInterpolate
import numpy as np


class DiffDivision(AbstractInterpolate):
    def _solve(self, x_known, y_known, x_interp):
        n = len(x_known)
        # Calcula as diferenças divididas
        divided_diff = np.zeros((n, n))
        divided_diff[:, 0] = y_known
        
        for j in range(1, n):
            for i in range(n-j):
                divided_diff[i, j] = (divided_diff[i+1, j-1] - divided_diff[i, j-1]) / (x_known[i+j] - x_known[i])
        
        # Realiza a interpolação usando diferenças divididas
        y_interp = divided_diff[0, 0]
        prod = 1
        for j in range(1, n):
            prod *= (x_interp - x_known[j-1])
            y_interp += divided_diff[0, j] * prod
        
        return y_interp