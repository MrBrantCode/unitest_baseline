"""
QUESTION:
For given an integer $n$, print all permutations of $\\{1, 2, ..., n\\}$ in lexicographic order.

Constraints

* $1 \leq n \leq 9$

Input

An integer $n$ is given in a line.

Output

Print each permutation in a line in order. Separate adjacency elements by a space character.

Examples

Input

2


Output

1 2
2 1


Input

3


Output

1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

from itertools import permutations

def generate_permutations(n: int) -> list[str]:
    """
    Generate all permutations of the numbers from 1 to n in lexicographic order.

    Parameters:
    - n (int): The number of elements to permute.

    Returns:
    - list[str]: A list of strings, where each string represents a permutation of the numbers from 1 to n.
    """
    # Generate permutations of the numbers from 1 to n
    perm = permutations(map(str, range(1, n + 1)))
    
    # Convert each permutation tuple to a space-separated string
    result = [' '.join(p) for p in perm]
    
    return result