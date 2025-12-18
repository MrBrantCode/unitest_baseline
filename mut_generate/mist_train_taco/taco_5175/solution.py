"""
QUESTION:
Snuke has a large collection of cards. Each card has an integer between 1 and N, inclusive, written on it. He has A_i cards with an integer i.

Two cards can form a pair if the absolute value of the difference of the integers written on them is at most 1.

Snuke wants to create the maximum number of pairs from his cards, on the condition that no card should be used in multiple pairs. Find the maximum number of pairs that he can create.

Constraints

* 1 ≦ N ≦ 10^5
* 0 ≦ A_i ≦ 10^9 (1 ≦ i ≦ N)
* All input values are integers.

Input

The input is given from Standard Input in the following format:


N
A_1
:
A_N


Output

Print the maximum number of pairs that Snuke can create.

Examples

Input

4
4
0
3
2


Output

4


Input

8
2
0
1
6
0
8
2
1


Output

9
"""

def max_card_pairs(N, A):
    count = 0
    mod = 0
    for i in range(N):
        b = A[i]
        if b == 0:
            mod = 0
        c = b + mod
        if not c == 0:
            count += c // 2
            mod = c % 2
    return count