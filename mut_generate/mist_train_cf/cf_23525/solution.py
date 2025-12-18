"""
QUESTION:
Create a function `count_vowels` that takes a string as input and returns the number of vowels in the string. The function should consider both lowercase and uppercase vowels. The input string only contains ASCII characters.
"""

def count_vowels(s):
    """
    This function takes a string as input and returns the number of vowels in the string.
    
    The function considers both lowercase and uppercase vowels.
    
    The input string only contains ASCII characters.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)