"""
QUESTION:
Create a function called `balancedStringSplit(s)` that takes a balanced string `s` as input, where `s` consists of only 'L' and 'R' characters and has an equal number of 'L' and 'R'. The function should return the maximum number of split balanced strings that can be formed, where each split string must have an equal number of 'L' and 'R' characters and at least one 'LR' or 'RL' pair. The length of `s` is between 1 and 1000.
"""

def balancedStringSplit(s):
    res = cnt = 0
    for c in s:
        cnt += 1 if c == 'L' else -1
        if cnt == 0:
            res += 1
    return res