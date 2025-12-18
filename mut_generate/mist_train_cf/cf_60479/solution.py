"""
QUESTION:
Split a string into the maximum amount of balanced substrings where the number of 'L's and 'R's are equal and the number of 'L's in the first half of the substring is equal to the number of 'R's in the second half of the substring. Implement a function named `balancedStringSplit` that takes a balanced string `s` as input, where `1 <= s.length <= 1000` and `s[i]` is either 'L' or 'R', and returns the maximum amount of split balanced strings that satisfy the new condition.
"""

def balancedStringSplit(s: str) -> int:
    count = l = r = 0
    for i in range(len(s)):
        if s[i] == 'L':
            l += 1
        else:
            r += 1
        if l == r and s[:i + 1].count('L') == s[i + 1:].count('R'):
            count += 1
            l = r = 0
    return count