"""
QUESTION:
Implement a function `solve_csp(constraints, individuals)` that takes in the following parameters:
- `constraints`: A list of dictionaries, each containing 'constraint_id', 'role_id', and 'condition'. 'condition' is a function that takes an individual's attributes and returns True if the individual satisfies the constraint, False otherwise.
- `individuals`: A list of dictionaries, each containing the attributes of an individual.

The function should return a dictionary mapping role IDs to the IDs of the individuals assigned to each role, satisfying all constraints. If no valid assignment is possible for a role, return an empty list for that role.
"""

def solve_csp(constraints, individuals):
    roles = {c['role_id']: [] for c in constraints}
    for individual in individuals:
        for role_id in roles:
            if all(constraint['condition'](individual) for constraint in constraints if constraint['role_id'] == role_id):
                roles[role_id].append(individual['id'])
    return roles