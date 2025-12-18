"""
QUESTION:
Takahashi had a pair of two positive integers not exceeding N, (a,b), which he has forgotten. He remembers that the remainder of a divided by b was greater than or equal to K. Find the number of possible pairs that he may have had.

Constraints

* 1 \leq N \leq 10^5
* 0 \leq K \leq N-1
* All input values are integers.

Input

Input is given from Standard Input in the following format:


N K


Output

Print the number of possible pairs that he may have had.

Examples

Input

5 2


Output

7


Input

10 0


Output

100


Input

31415 9265


Output

287927211
"""

def count_possible_pairs(N, K):
    ans = 0
    for i in range(1, N + 1):
        ans += N // i * max(0, i - K) + max(0, N % i - K + 1)
    if K == 0:
        ans -= N
    return ans