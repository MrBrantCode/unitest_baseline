"""
QUESTION:
Construct a function `characterCount(str)` that takes a string as input and returns a dictionary containing the count of each character present in the string. The function should be able to handle any type of characters in the string, including spaces and punctuation. The keys of the dictionary should be the characters from the string and the values should be their corresponding counts.
"""

def character_count(s):
    """
    Returns a dictionary containing the count of each character present in the input string.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary where keys are characters from the string and values are their corresponding counts.
    """
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq