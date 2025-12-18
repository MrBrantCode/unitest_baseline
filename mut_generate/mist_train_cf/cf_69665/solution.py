"""
QUESTION:
Write a function `reverse_in_place(s)` that takes a string `s` as input and returns the string with each word reversed without changing their original positions. The function should handle edge cases such as special characters, capitalization in the middle of words, and punctuation marks within and outside the words.
"""

def reverse_in_place(s):
    """
    The function splits the input string into a list of words. 
    Then it iterates through the list and reverse each word. 
    Finally, it joins the list back into a string with a space separator.
    """
    return ' '.join(word[::-1] for word in s.split(' '))