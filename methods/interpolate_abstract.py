class AbstractInterpolate():
    def _run_tests(self):
        # Define os pontos conhecidos
        x_known = [1, 2, 3, 4]
        y_known = [2, 1, 3, 2]
        
        # Interpolação para encontrar o valor em x = 2.5
        x_interp = 2.5
        y_interp = self._solve(x_known, y_known, x_interp)
        
        print(f"Interpolação para x = {x_interp}: y = {y_interp}")
    
    def _solve(self, x_known, y_known, x_interp):
        raise NotImplementedError