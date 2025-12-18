"""
QUESTION:
Write a function `min_seconds_to_palindrome(gemstones)` that takes a list of strings `gemstones` and returns the minimum number of seconds required to transform each string into a palindrome by removing characters. The function should return the total minimum seconds for all strings.
"""

def min_seconds_to_palindrome(gemstones):
    min_seconds = 0
    for gemstone in gemstones:
        left, right = 0, len(gemstone) - 1
        while left < right:
            if gemstone[left] != gemstone[right]:
                min_seconds += 1
                right -= 1
            else:
                left += 1
                right -= 1
    return min_seconds