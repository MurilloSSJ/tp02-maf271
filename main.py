from methods.gauss import GaussMethod
from methods.lu_decompose import LuDecompose
from methods.cholesky_decompose import CholeskyDecomposer
from methods.jacobi import Jacobi
from methods.gauss_seid import GaussSeidSolver
from methods.newton import NewtonSolver
from methods.newton_modified import NewtonModifiedSolver
from methods.lagrange import Lagrange
from methods.dff_finites import DiffFinites
from methods.diff_divisions import DiffDivision

#GaussMethod()._run_tests()
#LuDecompose()._run_tests()
#CholeskyDecomposer()._run_tests()
#Jacobi()._run_tests()
#GaussSeidSolver()._run_tests()
#NewtonSolver()._run_tests()
#NewtonModifiedSolver()._run_tests()
#Lagrange()._run_tests()
#DiffFinites()._run_tests()
DiffDivision()._run_tests()
