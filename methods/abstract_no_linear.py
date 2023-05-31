from sympy import symbols, Eq, Matrix
from sympy import diff, cos, sin
import numpy as np


class AbstractNoLinearSolver():
    def _solver(self):
        raise NotImplementedError
    
    def _run_tests(self):
        x, y, z = symbols('x y z')
        x_sym = [x, y, z]

        # Equations 1 and 2
        F = [cos(x) + y - z - 1, x**2 + y**2 - 4, x + y + z - 2]
        x0 = [1, 1, 1]  # Initial guess for the solution
        result = self._solve(F, x_sym, x0)
        print(result)
        F_val = [F[i].subs(list(zip(x_sym, result))) for i in range(len(F))]
        print(F_val)