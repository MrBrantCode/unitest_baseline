"""
QUESTION:
# Task
Given some sticks by an array `V` of positive integers, where V[i] represents the length of the sticks, find the number of ways we can choose three of them to form a triangle.

# Example

 For `V = [2, 3, 7, 4]`, the result should be `1`.

 There is only `(2, 3, 4)` can form a triangle.
 
 For `V = [5, 6, 7, 8]`, the result should be `4`.
 
 `(5, 6, 7), (5, 6, 8), (5, 7, 8), (6, 7, 8)` 

# Input/Output


 - `[input]` integer array `V`

 stick lengths
 
 `3 <= V.length <= 100`
 
 `0 < V[i] <=100`


 - `[output]` an integer

 number of ways we can choose 3 sticks to form a triangle.
"""

from itertools import combinations

def count_triangles(v):
    """
    Count the number of ways to choose three sticks from the list `v` that can form a triangle.

    Parameters:
    v (list of int): A list of positive integers representing the lengths of the sticks.

    Returns:
    int: The number of ways to choose three sticks that can form a triangle.
    """
    v.sort()
    return sum((a + b > c for (a, b, c) in combinations(v, 3)))