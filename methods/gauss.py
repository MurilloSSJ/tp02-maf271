from methods.abstract_resolver import AbstractResolver


class GaussMethod(AbstractResolver):
    def _solve(self, A, b):
        n = len(A)
        # Etapa de eliminação
        for i in range(n-1):
            # Verifica se o pivô é zero e realiza um pivoteamento parcial
            if A[i][i] == 0:
                for j in range(i+1, n):
                    if A[j][i] != 0:
                        A[i], A[j] = A[j], A[i]
                        b[i], b[j] = b[j], b[i]
                        break
            
            for j in range(i+1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                b[j] -= factor * b[i]
        
        x = [0] * n
        x[n-1] = b[n-1] / A[n-1][n-1]

        for i in range(n-2, -1, -1):
            sum = b[i]
            for j in range(i+1, n):
                sum -= A[i][j] * x[j]
            x[i] = sum / A[i][i]

        return x


