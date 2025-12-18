"""
QUESTION:
Create a function `length_of_longest_substring(s)` that takes a string `s` as input and returns the length of the longest continuous sequence of unique characters. The function should have a linear time complexity (O(n)), where n is the size of the string.
"""

def length_of_longest_substring(s):
    n = len(s)
    result = 0

    # Starting index of current
    # window to calculate max length
    window_start = 0

    # Dictionary to stored last index
    # of already visited character.
    ch_index = {}

    # Traverse through the given string.
    for window_end in range(0, n):

        # If current character is seen,
        # update start of window
        if s[window_end] in ch_index:
            window_start = max(ch_index[s[window_end]] + 1, window_start)

        # Update result if we get a larger window
        result = max(result, window_end - window_start + 1)

        # Update last index of current character.
        ch_index[s[window_end]] = window_end

    return result