"""
QUESTION:
Implement a function `minSwaps(s)` that takes a string `s` as input and returns the minimum number of swaps needed to rearrange the characters in `s` such that no two same characters are adjacent to each other. If it is impossible to rearrange the string, return -1.
"""

def minSwaps(s):
    # Count the frequency of each character
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1

    # Sort the characters based on their frequencies
    sorted_chars = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

    # Initialize the result string and pointers
    result = [''] * len(s)
    i = 0
    j = 1

    # Insert the characters in the result string
    for c in sorted_chars:
        # Check if it can be inserted at position i
        if i < len(s) and result[i] != c:
            result[i] = c
            i += 2
        # Check if it can be inserted at position j
        elif j < len(s) and result[j] != c:
            result[j] = c
            j += 2
        # If neither position i nor j is available, return -1
        else:
            return -1

    # Calculate the number of swaps needed
    swaps = abs(i - j) // 2

    return swaps