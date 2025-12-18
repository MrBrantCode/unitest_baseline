"""
QUESTION:
Create a function called `count_vowels` that calculates the number of vowels in a given alphanumeric phrase. The function should consider both lowercase and uppercase vowels.
"""

def count_vowels(phrase):
    """
    This function calculates the number of vowels in a given alphanumeric phrase.
    
    Parameters:
    phrase (str): The input string to count vowels from.
    
    Returns:
    int: The total count of vowels in the phrase.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return sum(1 for char in phrase if char in vowels)