from methods.interpolate_abstract import AbstractInterpolate
import numpy as np


class DiffFinites(AbstractInterpolate):
    def _solve(self, x_known, y_known, x_interp):
        n = len(x_known)
        
        # Calcula as diferenças finitas
        diff_y = np.diff(y_known)
        diff_x = np.diff(x_known)
        
        # Encontra o intervalo no qual o x_interp está
        interval = None
        for i in range(n-1):
            if x_known[i] <= x_interp <= x_known[i+1]:
                interval = i
                break
                
        # Realiza a interpolação usando diferenças finitas
        y_interp = y_known[interval] + (x_interp - x_known[interval]) * (diff_y[interval] / diff_x[interval])
        
        return y_interp