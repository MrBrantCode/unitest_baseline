"""
QUESTION:
Create a function called `create_sorted_dict()` that takes a string as input and returns a dictionary with the alphabetical order of the letters in the string. The string can contain uppercase and lowercase letters, special characters, and numbers, but the function should ignore any special characters or numbers. The function should handle cases where the input string is empty or consists only of special characters or numbers, and cases where the input string contains multiple occurrences of the same letter. The input string should have at least 5 characters and at most 100 characters. The function should return a dictionary where the keys are the unique letters in the string and the values are the frequency of each letter.
"""

def create_sorted_dict(input_string):
    """
    This function creates a dictionary from the alphabetical order of the letters in the input string.
    It ignores any special characters or numbers and handles cases with multiple occurrences of the same letter.
    
    Args:
        input_string (str): The input string to be processed.
    
    Returns:
        dict: A dictionary with unique letters in the string as keys and their frequency as values.
    """
    my_dict = {}
    
    for char in input_string:
        if char.isalpha():
            my_dict[char] = my_dict.get(char, 0) + 1
    
    return dict(sorted(my_dict.items()))