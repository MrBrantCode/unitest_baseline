"""
QUESTION:
Implement a function `process_matrix(valid, mask, rule_names, mt)` that takes in four parameters: 
- `valid`: a 2D boolean numpy array
- `mask`: a 2D boolean numpy array with the same shape as `valid`
- `rule_names`: a 1D numpy array of strings
- `mt`: a 1D numpy array of integers

The function should compute the product by iteratively processing `valid`, `mask`, and `rule_names`. 
In each iteration, it should find the row in `valid & mask` with exactly one `True` value, 
find the column index of this `True` value, and check if the corresponding rule name starts with "departure". 
If so, multiply the product by the value at the corresponding index in `mt`. 
Then, set all elements in the found column of `mask` to `False`. 
The function should return the final product after all elements in `mask` are `False`.
"""

import numpy as np

def process_matrix(valid, mask, rule_names, mt):
    product = 1
    while np.any(mask):
        cur = valid & mask
        axissum = cur.sum(axis=1)
        field = np.where(axissum == 1)[0][0]
        rule = np.where(cur[field, :])[0][0]
        if rule_names[rule].startswith("departure"):
            product *= int(mt[field])
        mask[:, rule] = False
    return product