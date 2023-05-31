from sympy import symbols, Eq, linear_eq_to_matrix


class AbstractResolver:
    def _solve(self, A, b):
        raise NotImplementedError
    
    def _run_tests(self):
        x, y, z, w = symbols('x y z w')
        eq1 = Eq(2*x + y, 5)
        eq2 = Eq(x - 3*y, -1)
        A, b = linear_eq_to_matrix([eq1, eq2], [x, y])
        result = self._solve(A.tolist(), list(b))
        eq1_response = int(eq1.args[0].subs({x:result[0], y:result[1]}))
        eq2_response = int(eq2.args[0].subs({x:result[0], y:result[1]}))
        print(f"Compare: expression: {eq1.args[0]}\t Response_data: {result}\t Result:{eq1_response}\t Expected:{eq1.args[1]}\n")
        print(f"Compare: expression: {eq2.args[0]}\t Response_data: {result}\t Result:{eq2_response}\t Expected:{eq2.args[1]}")
        print('----------------------------------')
        eq1 = Eq(3*x - 2*y + z, 4)
        eq2 = Eq(x + y + z, 2)
        eq3 = Eq(2*x - y + 2*z, 1)
        A, b = linear_eq_to_matrix([eq1, eq2, eq3], [x, y, z])
        result = self._solve(A.tolist(), list(b))
        eq1_response = int(eq1.args[0].subs({x:result[0], y:result[1], z:result[2]}))
        eq2_response = int(eq2.args[0].subs({x:result[0], y:result[1], z:result[2]}))
        eq3_response = int(eq3.args[0].subs({x:result[0], y:result[1], z:result[2]}))
        print(f"Compare: expression: {eq1.args[0]}\t Response_data: {result}\t Result:{eq1_response}\t Expected:{eq1.args[1]}\n")
        print(f"Compare: expression: {eq2.args[0]}\t Response_data: {result}\t Result:{eq2_response}\t Expected:{eq2.args[1]}\n")
        print(f"Compare: expression: {eq3.args[0]}\t Response_data: {result}\t Result:{eq3_response}\t Expected:{eq3.args[1]}")
        print('----------------------------------')
        eq1 = Eq(x + y + z + w, 1)
        eq2 = Eq(2*x - y - 3*z + w, 2)
        eq3 = Eq(3*x + y + 2*z - 2*w, 1)
        eq4 = Eq(x - 2*y + 3*z - 4*w, 0)
        A, b = linear_eq_to_matrix([eq1, eq2, eq3, eq4], [x, y, z, w])
        result = self._solve(A.tolist(), list(b))
        eq1_response = int(eq1.args[0].subs({x:result[0], y:result[1], z:result[2], w:result[3]}))
        eq2_response = int(eq2.args[0].subs({x:result[0], y:result[1], z:result[2], w:result[3]}))
        eq3_response = int(eq3.args[0].subs({x:result[0], y:result[1], z:result[2], w:result[3]}))
        eq4_response = int(eq4.args[0].subs({x:result[0], y: result[1], z:result[2], w:result[3]}))
        print(f"Compare: Expression: {eq1.args[0]}\t Response_data: {result}\t Result:{eq1_response}\t Expected:{eq1.args[1]}\n")
        print(f"Compare: Expression: {eq2.args[0]}\t Response_data: {result}\t Result:{eq2_response}\t Expected:{eq2.args[1]}\n")
        print(f"Compare: Expression: {eq3.args[0]}\t Response_data: {result}\t Result:{eq3_response}\t Expected:{eq3.args[1]}\n")
        print(f"Compare: Expression: {eq4.args[0]}\t Response_data: {result}\t Result:{eq4_response}\t Expected:{eq4.args[1]}")