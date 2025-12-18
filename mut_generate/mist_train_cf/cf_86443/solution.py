"""
QUESTION:
Write a function `longest_palindrome` that takes a character sequence as input and returns the longest palindromic substring. The function should have a time complexity of less than O(n^2) and a space complexity of less than O(n), where n is the length of the sequence. The sequence will not exceed 1000 characters in length.
"""

def longest_palindrome(s):
    # Transform the input string to a new string with '#' characters
    # to handle even-length palindromes as well
    t = '#'.join('^{}$'.format(s))

    # Create an array to store the length of the palindromic substring
    # centered at each character
    n = len(t)
    p = [0] * n

    # Current center and right boundary of the palindromic substring
    center = right = 0

    # Iterate through the transformed string
    for i in range(1, n - 1):
        # Find the mirror position of i
        mirror = 2 * center - i

        # Check if the mirror position is within the current palindromic substring
        if right > i:
            p[i] = min(right - i, p[mirror])

        # Expand the palindromic substring centered at i
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1

        # Check if the palindromic substring centered at i expands beyond the current right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]

    # Find the maximum length of the palindromic substring
    max_len = max(p)
    # Find the center index of the longest palindromic substring
    center_index = p.index(max_len)

    # Extract the longest palindromic substring from the transformed string
    start = (center_index - max_len) // 2
    end = start + max_len

    return s[start:end]