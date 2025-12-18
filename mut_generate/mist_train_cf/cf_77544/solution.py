"""
QUESTION:
Given a list of strings, write a function `splitLoopedString(strings)` that concatenates these strings together into a loop, allowing for string reversal, and finds the lexicographically largest string after cutting the loop to form a regular string. The order of concatenation should prioritize the string with the highest lexicographical value. The input strings only contain lowercase letters and have a total length of 1,000 or less.
"""

def splitLoopedString(strings):
    strings = [max(s, s[::-1]) for s in sorted(strings, reverse=True)]
    max_str = ''.join(strings)
    for i, s in enumerate(strings):
        r = s[::-1]
        strings[i] = ''
        max_str = max(max_str, ''.join(strings)+s, ''.join(strings)+r)
        for j in range(1, len(s)):
            max_str = max(max_str, ''.join(strings)+s[j:]+s[:j], ''.join(strings)+r[j:]+r[:j])
        strings[i] = s
    return max_str