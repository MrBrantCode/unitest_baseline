"""
QUESTION:
Write a function `reverse_string(string)` that takes a string of 3 to 15 uppercase letters and prints each letter in reverse order while counting the number of vowels in the string. The function should return the vowel count.
"""

def reverse_string(s):
    """
    This function takes a string of 3 to 15 uppercase letters, 
    prints each letter in reverse order, and counts the number of vowels in the string.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """

    def reverse_string_recursive(s):
        if len(s) == 1:  
            print(s)
            if s in 'AEIOU':  
                return 1  
            else:
                return 0
        else:
            print(s[-1])  
            if s[-1] in 'AEIOU':  
                return 1 + reverse_string_recursive(s[:-1])  
            else:
                return reverse_string_recursive(s[:-1])  

    return reverse_string_recursive(s)