"""
QUESTION:
Write a function `longest_palindrome_odd_distinct(s)` that returns the length of the longest palindromic substring of string `s` containing an odd number of distinct characters. The function should take a string `s` as input and return an integer representing the length of the longest palindromic substring with an odd number of distinct characters.
"""

def longest_palindrome_odd_distinct(s):
    n = len(s)
    longest = 0

    # Iterate through each character as the center of palindrome
    for i in range(n):
        # Expand the palindrome outward
        left = i
        right = i

        # Count distinct characters
        distinct = set()
        distinct.add(s[i])

        while left >= 0 and right < n and s[left] == s[right]:
            # Check if the palindrome has odd number of distinct characters
            if len(distinct) % 2 == 1:
                longest = max(longest, right - left + 1)

            # Expand the palindrome
            left -= 1
            right += 1

            # Update distinct characters
            if left >= 0:
                distinct.add(s[left])
            if right < n:
                distinct.add(s[right])

    return longest