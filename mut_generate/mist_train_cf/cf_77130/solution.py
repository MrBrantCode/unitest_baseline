"""
QUESTION:
Implement a function named `shortest_substring` that takes a string `s` as input and returns the length of the shortest substring without any repeating characters. The function should use a sliding window approach to efficiently find the shortest substring.
"""

def shortest_substring(s):
    used = {}  # maps characters to their latest positions
    start = 0  # start position of the current substring
    min_len = float('inf')  # smallest substring length

    for i, c in enumerate(s):
        if c in used and start <= used[c]:  # if c is in current substring
            start = used[c] + 1  # start from the next character
        else:  # if c is not in current substring
            min_len = min(min_len, i - start + 1)
        used[c] = i  # update latest position of c

    # If the string is all unique characters, min_len remains at infinity,
    # so return the string length instead
    return min_len if min_len != float('inf') else len(s)