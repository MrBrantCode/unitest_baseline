"""
QUESTION:
Create a function `count_vowels` that takes a string as input and returns a dictionary where the keys are the vowels in the string and the values are their respective counts. The function should be case-insensitive, meaning it should treat 'a' and 'A' as the same vowel. The function should only count the standard English vowels 'a', 'e', 'i', 'o', and 'u'.
"""

def count_vowels(sentence):
    """
    Returns a dictionary with vowels in the input string as keys and their respective counts as values.
    
    The function is case-insensitive and only counts the standard English vowels 'a', 'e', 'i', 'o', and 'u'.

    Args:
        sentence (str): The input string.

    Returns:
        dict: A dictionary with vowel counts.
    """
    sentence = sentence.lower()
    vowels = set("aeiou")
    vowel_counts = {}
    for char in sentence:
        if char in vowels:
            if char in vowel_counts:
                vowel_counts[char] += 1
            else:
                vowel_counts[char] = 1
    return vowel_counts