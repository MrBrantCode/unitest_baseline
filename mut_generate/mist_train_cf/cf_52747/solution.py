"""
QUESTION:
Write a function `countAndSay(n)` that calculates the sum of the digits in the nth term of the count-and-say sequence, where `1 <= n <= 30`. The count-and-say sequence is a sequence of digit strings defined by the recursive formula: `countAndSay(1) = "1"` and `countAndSay(n)` is the way you would "say" the digit string from `countAndSay(n-1)`, which is then converted into a different digit string. To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
"""

def countAndSay(n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
    return sum(map(int, s))