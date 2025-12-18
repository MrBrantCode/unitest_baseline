"""
QUESTION:
Create a function named `vowels_count` that takes a string `s` as input, representing a word. The function should return the total count of vowels present in the word. The vowels are 'a', 'e', 'i', 'o', 'u', and 'y' only when 'y' occurs as the last character of the word. The function should disregard case sensitivity and consider special characters.
"""

def vowels_count(s):
    """
    This function takes a string as input and returns the total count of vowels present in the word.
    The vowels are 'a', 'e', 'i', 'o', 'u', and 'y' only when 'y' occurs as the last character of the word.
    The function disregards case sensitivity and considers special characters.

    Parameters:
    s (str): The input string.

    Returns:
    int: The total count of vowels in the string.
    """
    vowels = "aeiou"
    count = 0
    s = s.lower()
    for char in s:
        if char in vowels:
            count += 1
    if s and s[-1] == 'y':
        count += 1

    return count