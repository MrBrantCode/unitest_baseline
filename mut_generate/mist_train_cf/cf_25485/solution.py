"""
QUESTION:
Write a function `generate_combinations` that takes a string as input and returns all possible combinations of contiguous substrings of that string. The function should include combinations of single characters and the entire string itself.
"""

def generate_combinations(string):
    """
    Generate all possible combinations of contiguous substrings of the input string.
    
    Args:
    string (str): The input string.
    
    Returns:
    list: A list of all possible combinations of contiguous substrings.
    """
    result = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            result.append(string[i:j])
    return result