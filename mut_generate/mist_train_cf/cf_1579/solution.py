"""
QUESTION:
Write a function named `find_longest_word` that takes a list of words as input and returns the longest word that starts with a vowel and ends with a consonant. The function should have a time complexity of O(n), where n is the number of words in the list, and should not use any built-in string manipulation or regular expression libraries.
"""

def find_longest_word(dictionary):
    """
    This function finds the longest word in a given dictionary that starts with a vowel and ends with a consonant.

    Parameters:
    dictionary (list): A list of words.

    Returns:
    str: The longest word that starts with a vowel and ends with a consonant.

    """
    longest_word = ""
    
    for word in dictionary:
        # Check if the word starts with a vowel and ends with a consonant
        if len(word) >= 8 and word[0].lower() in 'aeiou' and word[-1].lower() not in 'aeiou':
            # Update the longest word if the current word is longer
            if len(word) > len(longest_word):
                longest_word = word
    
    return longest_word