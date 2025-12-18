"""
QUESTION:
Write a function named `sum_vowels` that calculates the sum of the values of all lowercase vowels in a string, excluding any characters that are not letters. The function should ignore any vowels that are repeated consecutively more than two times. The value of a vowel is determined by its position in the alphabet, where 'a' is 1, 'b' is 2, and so on.
"""

def sum_vowels(s):
    """
    Calculate the sum of the values of all lowercase vowels in a string, 
    excluding any characters that are not letters. The function ignores any 
    vowels that are repeated consecutively more than two times. The value of 
    a vowel is determined by its position in the alphabet, where 'a' is 1, 
    'b' is 2, and so on.

    Args:
        s (str): The input string.

    Returns:
        int: The sum of the values of all lowercase vowels in the string.
    """

    vowels = "aeiou"
    sum_vowels = 0
    consecutive_count = 0

    for char in s.lower():
        if char.isalpha() and char in vowels:
            if consecutive_count < 2:
                sum_vowels += ord(char) - ord('a') + 1
                consecutive_count += 1
            else:
                consecutive_count = 0
        else:
            consecutive_count = 0

    return sum_vowels