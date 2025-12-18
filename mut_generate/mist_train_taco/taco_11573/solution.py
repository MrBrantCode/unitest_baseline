"""
QUESTION:
Snuke is interested in strings that satisfy the following conditions:

* The length of the string is at least N.
* The first N characters equal to the string s.
* The last N characters equal to the string t.



Find the length of the shortest string that satisfies the conditions.

Constraints

* 1≤N≤100
* The lengths of s and t are both N.
* s and t consist of lowercase English letters.

Input

The input is given from Standard Input in the following format:


N
s
t


Output

Print the length of the shortest string that satisfies the conditions.

Examples

Input

3
abc
cde


Output

5


Input

1
a
z


Output

2


Input

4
expr
expr


Output

4
"""

def find_shortest_string_length(N, s, t):
    x = s + t
    for i in range(N):
        if s[i:N] == t[0:N - i]:
            x = s + t[N - i:N]
            break
    return len(x)