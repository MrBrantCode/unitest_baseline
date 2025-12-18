"""
QUESTION:
Takahashi has a string S of length N consisting of lowercase English letters. On this string, he will perform the following operation K times:

* Let T be the string obtained by reversing S, and U be the string obtained by concatenating S and T in this order.
* Let S' be some contiguous substring of U with length N, and replace S with S'.



Among the strings that can be the string S after the K operations, find the lexicographically smallest possible one.

Constraints

* 1 \leq N \leq 5000
* 1 \leq K \leq 10^9
* |S|=N
* S consists of lowercase English letters.

Input

Input is given from Standard Input in the following format:


N K
S


Output

Print the lexicographically smallest possible string that can be the string S after the K operations.

Examples

Input

5 1
bacba


Output

aabca


Input

10 2
bbaabbbaab


Output

aaaabbaabb
"""

def find_lexicographically_smallest_string(n, k, s):
    u = s + s[::-1]
    t = min((u[i:i + n] for i in range(n + 1)))
    (i, h) = (0, t[0])
    for (i, c) in enumerate(t):
        if c != h:
            break
    j = i
    for _ in range(k - 1):
        j <<= 1
        if j >= n:
            return h * n
    return h * j + t[i:i + n - j]