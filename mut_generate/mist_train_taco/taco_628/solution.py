"""
QUESTION:
There is a sequence of length N: A_1, A_2, ..., A_N. Initially, this sequence is a permutation of 1, 2, ..., N.

On this sequence, Snuke can perform the following operation:

* Choose K consecutive elements in the sequence. Then, replace the value of each chosen element with the minimum value among the chosen elements.



Snuke would like to make all the elements in this sequence equal by repeating the operation above some number of times. Find the minimum number of operations required. It can be proved that, Under the constraints of this problem, this objective is always achievable.

Constraints

* 2 \leq K \leq N \leq 100000
* A_1, A_2, ..., A_N is a permutation of 1, 2, ..., N.

Input

Input is given from Standard Input in the following format:


N K
A_1 A_2 ... A_N


Output

Print the minimum number of operations required.

Examples

Input

4 3
2 3 1 4


Output

2


Input

3 3
1 2 3


Output

1


Input

8 3
7 3 1 8 4 6 2 5


Output

4
"""

import math

def minimum_operations_to_equalize(n, k, sequence):
    # The sequence is not actually used in the calculation, but it's included for completeness
    return math.ceil((n - k) / (k - 1) + 1)