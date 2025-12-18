"""
QUESTION:
We have a string s consisting of lowercase English letters. Snuke can perform the following operation repeatedly:

* Insert a letter `x` to any position in s of his choice, including the beginning and end of s.



Snuke's objective is to turn s into a palindrome. Determine whether the objective is achievable. If it is achievable, find the minimum number of operations required.

Constraints

* 1 \leq |s| \leq 10^5
* s consists of lowercase English letters.

Input

Input is given from Standard Input in the following format:


s


Output

If the objective is achievable, print the number of operations required. If it is not, print `-1` instead.

Examples

Input

xabxa


Output

2


Input

ab


Output

-1


Input

a


Output

0


Input

oxxx


Output

3
"""

def min_operations_to_palindrome(s: str) -> int:
    s = list(s)
    l = 0
    r = len(s) - 1
    cnt = 0
    
    while r - l > 0:
        if s[r] == s[l]:
            l += 1
            r -= 1
        elif s[r] != s[l] and s[r] == 'x':
            r -= 1
            cnt += 1
        elif s[r] != s[l] and s[l] == 'x':
            l += 1
            cnt += 1
        else:
            return -1
    
    return cnt