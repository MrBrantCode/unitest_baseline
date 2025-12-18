"""
QUESTION:
Given is a string S of length N consisting of lowercase English letters.
Snuke can do this operation any number of times: remove fox occurring as a substring from s and concatenate the remaining parts of s.
What is the minimum possible length of s after some number of operations by Snuke?

-----Constraints-----
 - 1 \leq N \leq 2 \times 10^{5}
 - s is a string of length N consisting of lowercase English letters.

-----Input-----
Input is given from Standard Input in the following format:
N
s

-----Print-----
Print the minimum possible length of s after some number of operations by Snuke.

-----Sample Input-----
6
icefox

-----Sample Output-----
3

 - By removing the fox at the end of icefox, we can turn s into ice.
"""

def minimize_string_length(S: str, N: int) -> int:
    ans = N
    stack = []
    
    for s in S:
        if s == 'f':
            stack.append(0)
        elif s == 'o':
            if stack and stack[-1] == 0:
                stack[-1] = 1
            else:
                stack = []
        elif s == 'x':
            if stack and stack[-1] == 1:
                stack.pop()
                ans -= 3
            else:
                stack = []
        else:
            stack = []
    
    return ans