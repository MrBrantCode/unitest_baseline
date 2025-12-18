"""
QUESTION:
Write a function named generate_combinations that takes a string as input and returns all possible combinations of letters in the string. The function should return combinations of varying lengths, from single characters to the entire string.
"""

def generate_combinations(s):
    """
    Generate all possible combinations of letters in a given string.

    Args:
        s (str): The input string.

    Returns:
        list: A list of all possible combinations of letters in the string.
    """
    def backtrack(start, path):
        # Add the current combination to the result list
        result.append(path)
        
        for i in range(start, len(s)):
            # Generate all combinations by adding each character to the current path
            backtrack(i + 1, path + s[i])
    
    result = []
    backtrack(0, "")
    # Remove the empty string from the result
    result = result[1:]
    return result