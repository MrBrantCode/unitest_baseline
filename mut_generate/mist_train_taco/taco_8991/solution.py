"""
QUESTION:
You are given integers N and K. Find the number of triples (a,b,c) of positive integers not greater than N such that a+b,b+c and c+a are all multiples of K. The order of a,b,c does matter, and some of them can be the same.

Constraints

* 1 \leq N,K \leq 2\times 10^5
* N and K are integers.

Input

Input is given from Standard Input in the following format:


N K


Output

Print the number of triples (a,b,c) of positive integers not greater than N such that a+b,b+c and c+a are all multiples of K.

Examples

Input

3 2


Output

9


Input

5 3


Output

1


Input

31415 9265


Output

27


Input

35897 932


Output

114191
"""

def count_valid_triples(N: int, K: int) -> int:
    ans = (N // K) ** 3
    if K % 2 == 0:
        ans += ((N + K // 2) // K) ** 3
    return ans