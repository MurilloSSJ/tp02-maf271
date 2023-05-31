from methods.abstract_no_linear import AbstractNoLinearSolver
import numpy as np
from sympy import Matrix
from sympy import diff


class NewtonSolver(AbstractNoLinearSolver):
    def _solve(self, F, x, x0, max_iterations=100, tolerance=1e-6):
        n = len(x)
        J = Matrix([[diff(F[i], x[j]) for j in range(n)] for i in range(n)])

        x_vals = np.array(x0, dtype=float)

        for _ in range(max_iterations):
            F_val = np.array([F[i].subs(list(zip(x, x_vals))) for i in range(n)], dtype=float)
            J_val = np.array([[J[i, j].subs(list(zip(x, x_vals))) for j in range(n)] for i in range(n)], dtype=float)

            delta_x = np.linalg.solve(J_val, -F_val)
            x_vals = x_vals + delta_x

            if np.linalg.norm(delta_x) < tolerance:
                break

        return x_vals


