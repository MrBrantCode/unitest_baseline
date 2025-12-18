"""
QUESTION:
Determine if we can choose K different integers between 1 and N (inclusive) so that no two of them differ by 1.

Constraints

* 1\leq N,K\leq 100
* N and K are integers.

Input

Input is given from Standard Input in the following format:


N K


Output

If we can choose K integers as above, print `YES`; otherwise, print `NO`.

Examples

Input

3 2


Output

YES


Input

5 5


Output

NO


Input

31 10


Output

YES


Input

10 90


Output

NO
"""

def can_choose_k_integers(N: int, K: int) -> str:
    if 2 * K - 1 <= N:
        return "YES"
    else:
        return "NO"