"""
QUESTION:
# Task
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements.

Given two arrays, check whether they are similar.

# Example

For `A = [1, 2, 3]` and `B = [1, 2, 3]`, the output should be `true;`

For `A = [1, 2, 3]` and `B = [2, 1, 3]`, the output should be `true;`

For `A = [1, 2, 2]` and `B = [2, 1, 1]`, the output should be `false.`

# Input/Output

- `[input]` integer array `A`

Array of integers.

Constraints: `3 ≤ A.length ≤ 10000, 1 ≤ A[i] ≤ 1000.`

- `[input]` integer array `B`

Array of integers of the same length as `A`.

Constraints: `B.length = A.length, 1 ≤ B[i] ≤ 1000.`

- `[output]` a boolean value

`true` if `A` and `B` are similar, `false` otherwise.
"""

def are_similar(a, b):
    # Check if both arrays are already identical
    if a == b:
        return True
    
    # Check if sorting both arrays makes them identical
    if sorted(a) != sorted(b):
        return False
    
    # Count the number of positions where the elements differ
    diff_count = sum(1 for i, j in zip(a, b) if i != j)
    
    # Arrays are similar if they differ in exactly 2 positions
    return diff_count == 2