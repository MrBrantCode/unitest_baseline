"""
QUESTION:
Create a function named `sort_dictionary` that takes a dictionary as input and returns a sorted list of its key-value pairs. The sorting should be case-insensitive and based on the number of vowels in the keys in descending order. If two keys have the same number of vowels, they should be sorted by the number of consonants in the keys in descending order. The keys are strings.
"""

def sort_dictionary(dictionary):
    """
    Sorts a dictionary based on the number of vowels in its keys in descending order.
    If two keys have the same number of vowels, they are sorted by the number of consonants in the keys in descending order.

    Args:
        dictionary (dict): The dictionary to be sorted.

    Returns:
        list: A sorted list of key-value pairs from the dictionary.
    """
    vowels = set('aeiou')
    consonants = set('bcdfghjklmnpqrstvwxyz')
    
    def count_letters(word):
        count_vowels = sum(letter in vowels for letter in word.lower())
        count_consonants = sum(letter in consonants for letter in word.lower())
        return (-count_vowels, -count_consonants)

    return sorted(dictionary.items(), key=lambda item: count_letters(item[0]))