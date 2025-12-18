"""
QUESTION:
Implement a Python function `calculate_lipschitz_constant` that calculates the Lipschitz constant of a given function over a specified domain. The function should handle both scalar and vector-valued functions.

The function should have the following signature:
```python
def calculate_lipschitz_constant(func, domain):
```
Where:
- `func`: A Python function representing the function for which the Lipschitz constant needs to be calculated.
- `domain`: A list or array representing the domain over which the Lipschitz constant should be calculated.
"""

import numpy as np

def calculate_lipschitz_constant(func, domain):
    # Initialize the Lipschitz constant to a very small value
    lipschitz_constant = 1e-10
    
    # Iterate over the domain to find the maximum Lipschitz constant
    for x in domain:
        # Calculate the difference in function values for nearby points
        delta_f = np.abs(func(x + 1e-8) - func(x))
        
        # Calculate the difference in domain points
        delta_x = 1e-8
        
        # Update the Lipschitz constant if a larger value is found
        lipschitz_constant = max(lipschitz_constant, delta_f / delta_x)
    
    return lipschitz_constant