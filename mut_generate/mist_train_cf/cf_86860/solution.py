"""
QUESTION:
Implement a function `count_unique_substrings(s)` that calculates the number of unique substrings possible with the given string `s`. The function should only consider substrings that do not contain any repeated characters. The length of `s` will not exceed 1000 characters and can contain lowercase letters, uppercase letters, digits, and special characters. The solution should have a time complexity of O(n^2), where n is the length of the string.
"""

def count_unique_substrings(s):
    n = len(s)
    count = 0

    # Iterate over all possible substrings
    for i in range(n):
        for j in range(i, n):
            # Check if the substring contains any repeated characters
            substring = s[i:j+1]
            if len(set(substring)) == len(substring):
                count += 1

    return count