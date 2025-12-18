"""
QUESTION:
Implement a function `is_solver_available(solver_name: str) -> bool` that checks if a given iterative linear solver is available. The function should return `True` if the solver is available and `False` otherwise. The available solvers are 'GMRES', 'FGMRES', 'CG', 'CR', 'CGNR', 'CGNE', 'BiCGSTAB', 'Steepest Descent', 'Minimal Residual'. The function should be case-sensitive and match the solver name exactly.
"""

def is_solver_available(solver_name: str) -> bool:
    available_solvers = ['GMRES', 'FGMRES', 'CG', 'CR', 'CGNR', 'CGNE', 'BiCGSTAB', 'Steepest Descent', 'Minimal Residual']
    return solver_name in available_solvers