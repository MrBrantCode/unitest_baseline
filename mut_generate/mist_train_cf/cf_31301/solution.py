"""
QUESTION:
Implement the `prolog_next_solution` function, which takes an environment `env` as input and returns `True` if there is a next solution, and updates the `vars` dictionary with the bindings for the variables in the query. The `vars` dictionary contains variable names as keys and their corresponding bindings as values. Additionally, implement the `str` function for Prolog data structures, which should return a string representation of the data in a specific format. The `env` object has `has_next_solution` and `get_next_solution` methods.
"""

def prolog_next_solution(env):
    if env.has_next_solution():
        vars = env.get_next_solution()
        return True
    else:
        return False