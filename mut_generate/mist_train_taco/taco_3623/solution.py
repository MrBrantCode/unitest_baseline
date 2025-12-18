"""
QUESTION:
You are given a string S of length N. Among its subsequences, count the ones such that all characters are different, modulo 10^9+7. Two subsequences are considered different if their characters come from different positions in the string, even if they are the same as strings.

Here, a subsequence of a string is a concatenation of one or more characters from the string without changing the order.

Constraints

* 1 \leq N \leq 100000
* S consists of lowercase English letters.
* |S|=N

Input

Input is given from Standard Input in the following format:


N
S


Output

Print the number of the subsequences such that all characters are different, modulo 10^9+7.

Examples

Input

4
abcd


Output

15


Input

3
baa


Output

5


Input

5
abcab


Output

17
"""

from collections import Counter

def count_unique_subsequences(S, N):
    mod = 10 ** 9 + 7
    s_c = Counter(S)
    ans = 1
    for c in s_c.values():
        ans *= c + 1
    return (ans - 1) % mod