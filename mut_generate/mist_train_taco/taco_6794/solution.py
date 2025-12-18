"""
QUESTION:
For a string S, let f(S) be the lexicographically smallest cyclic shift of S. For example, if S = `babca`, f(S) = `ababc` because this is the smallest among all cyclic shifts (`babca`, `abcab`, `bcaba`, `cabab`, `ababc`).

You are given three integers X, Y, and Z. You want to construct a string T that consists of exactly X `a`s, exactly Y `b`s, and exactly Z `c`s. If there are multiple such strings, you want to choose one that maximizes f(T) lexicographically.

Compute the lexicographically largest possible value of f(T).

Constraints

* 1 \leq X + Y + Z \leq 50
* X, Y, Z are non-negative integers.

Input

Input is given from Standard Input in the following format:


X Y Z


Output

Print the answer.

Examples

Input

2 2 0


Output

abab


Input

1 1 1


Output

acb
"""

def largest_cyclic_shift(X: int, Y: int, Z: int) -> str:
    # Create a list of lists where each sublist represents a character
    L = [[0] for _ in range(X)] + [[1] for _ in range(Y)] + [[2] for _ in range(Z)]
    
    # Merge the lists while maintaining the order
    while len(L) > 1:
        L[0] += L.pop()
        L.sort()
    
    # Convert the final list to a string
    result = ''.join((('a', 'b', 'c')[i] for i in L[0]))
    
    return result