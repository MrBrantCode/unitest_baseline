"""
ORIGINAL QUESTION:
Write a Python function `sort_vowel_keys` that sorts a dictionary by its keys in descending order, but only includes keys that start with a vowel, and returns the sorted dictionary along with the total number of vowels in the dictionary. The function should take one argument, a dictionary.
"""

def sort_vowel_keys(myDict):
    """
    Sorts a dictionary by its keys in descending order, 
    but only includes keys that start with a vowel, 
    and returns the sorted dictionary along with the total number of vowels in the dictionary.

    Args:
    myDict (dict): The input dictionary.

    Returns:
    tuple: A tuple containing the sorted dictionary and the total number of vowels.
    """
    vowel_keys = [key for key in myDict if key[0].lower() in 'aeiou']
    vowel_keys.sort(reverse=True)
    
    sorted_dict = {key: myDict[key] for key in vowel_keys}
    total_vowels = sum(myDict[key] for key in vowel_keys)

    return sorted_dict, total_vowels