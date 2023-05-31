from methods.abstract_no_linear import AbstractNoLinearSolver
import numpy as np
from sympy import diff

class NewtonModifiedSolver(AbstractNoLinearSolver):
    def _solve(self, F, x, x0, max_iterations=100, tolerance=1e-6):
        n = len(x)
        J = np.zeros((n, n), dtype=float)

        x_vals = np.array(x0, dtype=float)

        for _ in range(max_iterations):
            F_val = np.array([F[i].subs(list(zip(x, x_vals))) for i in range(n)], dtype=float)

            for i in range(n):
                for j in range(n):
                    J[i, j] = diff(F[i], x[j]).subs(list(zip(x, x_vals)))

            delta_x = np.linalg.solve(J, -F_val)
            x_vals = x_vals + delta_x

            if np.linalg.norm(delta_x) < tolerance:
                break

        return x_vals