"""
QUESTION:
You're given a string of lower-case Latin letters. Your task is to find the length of its longest substring that can be met in the string at least twice. These occurrences can overlap (see sample test 2).

Input

The first input line contains the string. It's guaranteed, that the string is non-empty, consists of lower-case Latin letters, and its length doesn't exceed 100.

Output

Output one number — length of the longest substring that can be met in the string at least twice.

Examples

Input

abcd


Output

0

Input

ababa


Output

3

Input

zzz


Output

2
"""

def longest_repeating_substring_length(s: str) -> int:
    k = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            x = s[i:j]
            for t in range(i + 1, len(s)):
                if x == s[t:t + j - i]:
                    k.append(j - i)
    return max(k) if k else 0