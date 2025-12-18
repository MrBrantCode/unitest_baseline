"""
QUESTION:
There are N rabbits, numbered 1 through N.

The i-th (1≤i≤N) rabbit likes rabbit a_i. Note that no rabbit can like itself, that is, a_i≠i.

For a pair of rabbits i and j (i＜j), we call the pair (i，j) a friendly pair if the following condition is met.

* Rabbit i likes rabbit j and rabbit j likes rabbit i.



Calculate the number of the friendly pairs.

Constraints

* 2≤N≤10^5
* 1≤a_i≤N
* a_i≠i

Input

The input is given from Standard Input in the following format:


N
a_1 a_2 ... a_N


Output

Print the number of the friendly pairs.

Examples

Input

4
2 1 4 3


Output

2


Input

3
2 3 1


Output

0


Input

5
5 5 5 5 1


Output

1
"""

def count_friendly_pairs(N, likes):
    ans = 0
    for i in range(N):
        if likes[likes[i] - 1] == i + 1:
            ans += 1
    return ans // 2