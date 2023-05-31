from methods.interpolate_abstract import AbstractInterpolate


class Lagrange(AbstractInterpolate):
    def _solve(self, x_known, y_known, x_interp):
        n = len(x_known)
        y_interp = 0.0
        
        for i in range(n):
            term = y_known[i]
            for j in range(n):
                if j != i:
                    term *= (x_interp - x_known[j]) / (x_known[i] - x_known[j])
            y_interp += term
        
        return y_interp