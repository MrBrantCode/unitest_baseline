"""
QUESTION:
Calculate the number of items in a vector that appear at the same index in each vector, with the same value. 

```python
   vector_affinity([1, 2, 3, 4, 5], [1, 2, 2, 4, 3]) # => 0.6
   vector_affinity([1, 2, 3], [1, 2, 3]) # => 1.0
```

Affinity value should be realized on a scale of 0.0 to 1.0, with 1.0 being absolutely identical. Two identical sets should always be evaulated as having an affinity or 1.0.

Hint: The last example test case holds a significant clue to calculating the affinity correctly.
"""

def calculate_vector_affinity(a, b):
    """
    Calculate the affinity between two vectors based on the number of items that appear at the same index
    with the same value. The affinity is scaled between 0.0 and 1.0, with 1.0 indicating absolute identity.

    Parameters:
    a (list): The first vector.
    b (list): The second vector.

    Returns:
    float: The affinity value between the two vectors.
    """
    longer = len(a) if len(a) > len(b) else len(b)
    if longer == 0:
        return 1.0
    matching_indices = [i for i, (x, y) in enumerate(zip(a, b)) if x == y]
    return len(matching_indices) / float(longer)