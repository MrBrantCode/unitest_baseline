"""
QUESTION:
Create a function named 'sort_strings' that sorts an array of strings lexicographically in reverse order, excluding any strings that start with a vowel. The function should take an array of strings as input and return the sorted array. The vowels to consider are 'a', 'e', 'i', 'o', and 'u'.
"""

def sort_strings(arr):
    """
    Sorts an array of strings lexicographically in reverse order, excluding any strings that start with a vowel.

    Parameters:
    arr (list): The input array of strings.

    Returns:
    list: The sorted array of strings.
    """
    vowels = 'aeiou'
    return sorted([s for s in arr if s[0].lower() not in vowels], reverse=True)