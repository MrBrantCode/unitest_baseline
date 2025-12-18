"""
QUESTION:
Write a function `findMaxSubstring(string)` that finds the maximum substring with a prime length and contains only unique characters in a given string of length n (n <= 10^6). The function should return the maximum substring that meets these conditions.

The function should iterate through each character in the string and check all possible prime lengths. The prime lengths should be restricted to numbers less than or equal to the length of the string. The function should return an empty string if no such substring exists.
"""

def findMaxSubstring(s):
    """
    Finds the maximum substring with a prime length and contains only unique characters in a given string.

    Args:
    s (str): The input string.

    Returns:
    str: The maximum substring that meets the conditions.
    """

    def is_prime(n):
        """Checks if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_unique(substring):
        """Checks if a substring contains only unique characters."""
        return len(substring) == len(set(substring))

    max_length = 0
    max_substring = ""
    for length in range(2, len(s) + 1):
        if is_prime(length):
            for i in range(len(s) - length + 1):
                substring = s[i:i + length]
                if is_unique(substring) and length > max_length:
                    max_length = length
                    max_substring = substring

    return max_substring