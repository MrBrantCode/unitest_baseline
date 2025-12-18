"""
QUESTION:
Implement a function `minSwaps(string)` that takes a string of lowercase letters as input and returns the minimum number of swaps needed to rearrange the string such that no two same characters are adjacent. If it is impossible to rearrange the string, return -1. The length of the input string will not exceed 10^5 and the time complexity of the solution should be O(n), where n is the length of the input string.
"""

def minSwaps(string):
    """
    Returns the minimum number of swaps needed to rearrange the string 
    such that no two same characters are adjacent. If it is impossible 
    to rearrange the string, return -1.

    Args:
        string (str): A string of lowercase letters.

    Returns:
        int: The minimum number of swaps needed.
    """
    # dictionary to store frequency of characters
    freq = {}
    for char in string:
        freq[char] = freq.get(char, 0) + 1

    # Sort the characters of the input string in descending order of their frequency
    sorted_chars = sorted(string, key=lambda x: freq[x], reverse=True)

    swaps = 0
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i+1]:
            # Find a different character to swap with the next position
            for j in range(i+2, len(sorted_chars)):
                if sorted_chars[j] != sorted_chars[i]:
                    sorted_chars[i+1], sorted_chars[j] = sorted_chars[j], sorted_chars[i+1]
                    swaps += 1
                    break
            else:
                return -1  # Cannot find a different character to swap with the next position

    return swaps