"""
QUESTION:
Given a binary string s representing a number, return the number of steps to reduce it to 1 under the following rules:
- If the current number is divisible by 3, subtract 1 from it.
- If the current number is even, divide it by 2.
- If the current number is odd, add 1 to it.

Constraints:
- 1 <= s.length <= 500
- s consists of characters '0' or '1'
- s[0] == '1'

Implement a function `numSteps(s: str) -> int` to solve the problem.
"""

def numSteps(s: str) -> int:
    s = list(map(int, s))
    ans = 0
    while True:
        if len(s) == 1 and s[0] == 1:
            return ans

        if s[-1] == 0: # number is even
            s.pop() # divide by 2
        else: # number is odd
            i = len(s) - 1
            while i >= 0 and s[i] == 1: 
                s[i] = 0 # set all bits from rightmost bit to first 0-bit to 0
                i -= 1
            if i >= 0:
                s[i] = 1 # set first 0-bit to 1
            else:
                s.insert(0, 1) # prepend 1 if all bits are 1
        ans += 1