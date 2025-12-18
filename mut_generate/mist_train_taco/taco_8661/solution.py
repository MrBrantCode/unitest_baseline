"""
QUESTION:
Snuke has N integers. Among them, the smallest is A, and the largest is B. We are interested in the sum of those N integers. How many different possible sums there are?

Constraints

* 1 ≤ N,A,B ≤ 10^9
* A and B are integers.

Input

Input is given from Standard Input in the following format:


N A B


Output

Print the number of the different possible sums.

Examples

Input

4 4 6


Output

5


Input

5 4 3


Output

0


Input

1 7 10


Output

0


Input

1 3 3


Output

1
"""

def count_possible_sums(N, A, B):
    if N == 1:
        return int(A == B)
    elif A > B:
        return 0
    else:
        return (B - A) * (N - 2) + 1