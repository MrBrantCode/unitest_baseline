"""
QUESTION:
Find places where a string P is found within a text T. Print all indices of T where P found. The indices of T start with 0.

Constraints

* 1 ≤ length of T ≤ 1000
* 1 ≤ length of P ≤ 1000
* The input consists of alphabetical characters and digits

Input

In the first line, a text T is given. In the second line, a string P is given.

Examples

Input

aabaaa
aa


Output

0
3
4


Input

xyzz
yz


Output

1


Input

abc
xyz


Output
"""

def find_pattern_indices(T: str, P: str) -> list[int]:
    if len(P) > len(T):
        return []
    
    p = len(P)
    ans = []
    
    for i in range(len(T) - len(P) + 1):
        if T[i:i + p] == P:
            ans.append(i)
    
    return ans