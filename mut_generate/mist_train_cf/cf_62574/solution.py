"""
QUESTION:
Create a function called `divergent_array` that takes a list of words as input and returns a new list containing only the words that include the character 'e'.
"""

def divergent_array(word_list):
    """Returns a list of words containing the character 'e'."""
    return [word for word in word_list if 'e' in word]