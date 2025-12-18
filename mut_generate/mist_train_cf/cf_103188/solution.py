"""
QUESTION:
Write a function called `compare_ascii` that takes two string arguments. The function should compare the ASCII values of the characters in the two input strings and return the string with the greater total ASCII value. If the total ASCII values of the two strings are equal, the function should return "Equal".
"""

def compare_ascii(s1, s2):
    """
    This function compares the total ASCII values of two input strings.
    It returns the string with the greater total ASCII value. 
    If the total ASCII values are equal, it returns "Equal".
    
    Parameters:
    s1 (str): The first input string.
    s2 (str): The second input string.
    
    Returns:
    str: The string with the greater total ASCII value or "Equal" if they are equal.
    """
    sum_s1 = sum(ord(c) for c in s1)
    sum_s2 = sum(ord(c) for c in s2)
    if sum_s1 > sum_s2:
        return s1
    elif sum_s1 < sum_s2:
        return s2
    else:
        return "Equal"