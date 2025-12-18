"""
QUESTION:
Write a function called `compress(s)` to compress a given string `s`. The function should return a new string consisting of each character in `s` followed by the count of consecutive occurrences of that character. The time complexity should be O(n), where n is the length of the input string, and the space complexity should be O(1), meaning that the function should compress the string in-place without using any additional data structures.
"""

def compress(s):
    if not s:
        return ""

    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))
    return ''.join(compressed)