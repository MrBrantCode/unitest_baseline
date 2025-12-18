"""
QUESTION:
You are given two integers K and S.
Three variable X, Y and Z takes integer values satisfying 0≤X,Y,Z≤K.
How many different assignments of values to X, Y and Z are there such that X + Y + Z = S?

Constraints

* 2≤K≤2500
* 0≤S≤3K
* K and S are integers.

Input

The input is given from Standard Input in the following format:


K S


Output

Print the number of the triples of X, Y and Z that satisfy the condition.

Examples

Input

2 2


Output

6


Input

5 15


Output

1
"""

def count_valid_triples(K, S):
    count = 0
    for x in range(K + 1):
        for y in range(K + 1):
            z = S - x - y
            if 0 <= z <= K:
                count += 1
    return count