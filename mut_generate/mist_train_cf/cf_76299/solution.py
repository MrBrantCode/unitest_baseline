"""
QUESTION:
Create a function `maxGridProductivity(p, q, workersCount, managersCount)` that takes four integers as input: `p`, `q`, `workersCount`, and `managersCount`, where `p` and `q` represent the dimensions of a grid, `workersCount` is the number of workers, and `managersCount` is the number of managers. The function should return the maximum possible grid productivity. The constraints are `1 <= p, q <= 5` and `0 <= workersCount, managersCount <= min(p * q, 6)`.
"""

import itertools

def maxGridProductivity(p, q, workersCount, managersCount):
    max_productivity = 0
    grid_size = p * q
    
    # Generate all possible combinations of workers and managers
    for worker_placements in itertools.combinations(range(grid_size + 1), workersCount):
        for manager_placements in itertools.combinations(range(grid_size + 1), managersCount):
            # Calculate productivity for each employee
            productivity = 0
            for i in range(workersCount):
                if worker_placements[i] != grid_size:  # Check if worker is assigned to a cell
                    productivity += (worker_placements[i] % p) + 1
            for i in range(managersCount):
                if manager_placements[i] != grid_size:  # Check if manager is assigned to a cell
                    productivity += (manager_placements[i] // p) + 1
            
            # Update maximum productivity
            max_productivity = max(max_productivity, productivity)
    
    return max_productivity