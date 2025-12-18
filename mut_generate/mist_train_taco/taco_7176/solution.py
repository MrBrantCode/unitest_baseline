"""
QUESTION:
Snuke can change a string t of length N into a string t' of length N - 1 under the following rule:

* For each i (1 ≤ i ≤ N - 1), the i-th character of t' must be either the i-th or (i + 1)-th character of t.



There is a string s consisting of lowercase English letters. Snuke's objective is to apply the above operation to s repeatedly so that all the characters in s are the same. Find the minimum necessary number of operations.

Constraints

* 1 ≤ |s| ≤ 100
* s consists of lowercase English letters.

Input

Input is given from Standard Input in the following format:


s


Output

Print the minimum necessary number of operations to achieve the objective.

Examples

Input

serval


Output

3


Input

jackal


Output

2


Input

zzz


Output

0


Input

whbrjpjyhsrywlqjxdbrbaomnw


Output

8
"""

def min_operations_to_uniform_string(s: str) -> int:
    l = len(s)
    d, a = {}, {}
    
    for i, c in enumerate(s):
        if c in d:
            d[c] = max(d[c], i - a[c])
        else:
            d[c] = i
        a[c] = i + 1
    
    for c, v in d.items():
        d[c] = max(v, l - a[c])
    
    return min(d.values())