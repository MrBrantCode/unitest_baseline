"""
QUESTION:
Implement a class for solving optimization problems using the Gurobi optimization solver with two modes: standard and decomposed. 

Implement the `GurobiStandardModel` class with the following methods: 
- `__init__(model)`: Initialize the model.
- `construct()`: Set up the standard model.
- `update_upper_bound(tracker)`: Update the upper bound using the tracker.
- `run()`: Execute the solver.
- `get_primals()`: Retrieve the primal solution.

Implement the `GurobiDecomposedModel` class with the following methods:
- `__init__(model, tracker)`: Initialize the model with a tracker.
- `construct()`: Set up the decomposed model.
- `update_upper_bound()`: Update the upper bound for the decomposed model.
- `run()`: Execute the solver for the decomposed model.
- `get_primals()`: Retrieve the primal solution for the decomposed model.
"""

def entrance(s: str) -> bool:
    return s == s[::-1]