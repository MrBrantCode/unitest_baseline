"""
QUESTION:
Write an algorithm for the function `longest_palindromic_substring(s)` that finds the longest palindromic substring of a given input string `s`. The function should have a time complexity of O(n) and should not use any extra space other than a constant amount of additional memory. The input string can contain any characters, including special characters and spaces. The function should not use any string manipulation functions or methods, such as reverse() or substr(), or any library functions that directly solve the problem. The input string will have a length of at most 10^5.
"""

def longest_palindromic_substring(s):
    if len(s) < 2:
        return s

    # Insert special character between each pair of characters
    t = '#' + '#'.join(s) + '#'

    # Initialize variables
    p = [0] * len(t)
    center = 0
    right = 0

    # Iterate over each character in t
    for i in range(len(t)):
        # Calculate p[i] using symmetry property
        if center - right < i:
            mirror = 2 * center - i
            if mirror >= 0 and i < right:
                p[i] = min(right - i, p[mirror])

        # Expand palindrome centered at i
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < len(t) and t[i - p[i] - 1] == t[i + p[i] + 1]:
            p[i] += 1

        # Update center and right if palindrome extends beyond current right boundary
        if i + p[i] > right:
            center = i
            right = i + p[i]

    # Find maximum value in p array
    max_value = max(p)

    # Find index of maximum value in p array
    index = p.index(max_value)

    # Calculate starting index of longest palindromic substring
    start = (index - max_value + 1) // 2

    # Extract longest palindromic substring from input string
    longest_palindrome = s[start: start + max_value]

    return longest_palindrome