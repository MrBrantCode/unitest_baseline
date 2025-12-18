"""
QUESTION:
Create a function called `filter_words` that takes a list of words as input and returns a new list containing only the words that have more than 3 vowels and end with a consonant. A consonant is any alphabet letter that is not a vowel. The function should be case-insensitive. The list should not be modified in place.
"""

def filter_words(lst):
    """
    Returns a new list containing only the words that have more than 3 vowels and end with a consonant.
    
    Args:
        lst (list): A list of words.
    
    Returns:
        list: A new list containing the filtered words.
    """
    return [word for word in lst if sum(1 for c in word if c.lower() in 'aeiou') > 3 and word[-1].lower() not in 'aeiou']