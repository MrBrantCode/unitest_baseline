"""
QUESTION:
Write a function called `count_vowels` that takes a string as input and returns the number of vowels in the string. The input string can contain any combination of letters, numbers, and special characters, but the function should only count the vowels 'a', 'e', 'i', 'o', and 'u' regardless of case.
"""

def count_vowels(sentence):
    """
    Count the number of vowels in the given sentence.

    Args:
        sentence (str): The input string to count vowels from.

    Returns:
        int: The number of vowels in the sentence.
    """
    return sum(1 for char in sentence.lower() if char in 'aeiou')