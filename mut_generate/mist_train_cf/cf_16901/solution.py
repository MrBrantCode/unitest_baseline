"""
QUESTION:
Write a function `find_longest_vowel_word` that finds the longest word in a given string that starts with a vowel, regardless of case. If no word starting with a vowel is present, the function should return a message indicating this. The input string may contain a mix of letters, numbers, and spaces.
"""

def find_longest_vowel_word(sample_string):
    """
    Finds the longest word in a given string that starts with a vowel, regardless of case.

    Args:
        sample_string (str): The input string.

    Returns:
        str: The longest word starting with a vowel, or a message if none is found.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    longest_word = ""
    for word in sample_string.split():
        if word[0].lower() in vowels:  
            if len(word) > len(longest_word):
                longest_word = word
    if longest_word:
        return longest_word
    else:
        return "No word starting with a vowel found in the string."