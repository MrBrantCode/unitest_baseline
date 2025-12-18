"""
QUESTION:
Write a function named `make_palindrome` that takes a string `text` as input. The function should convert the input string into a palindrome while maintaining the original characters and their order. It should also identify and return any words in the text that are already palindromes. The function should handle non-string inputs and empty strings gracefully without crashing. The time complexity of the function should not exceed O(n log n), where n is the length of the string.
"""

def make_palindrome(text):
    """
    This function takes a string input, converts it into a palindrome while maintaining 
    the original characters and their order, and identifies any words in the text that 
    are already palindromes.

    Args:
    text (str): The input string.

    Returns:
    tuple: A tuple containing the palindrome string and a list of palindromes found in the text.
    """

    if not isinstance(text, str):
        print("The input must be a string.")
        return None
    elif not text:
        print("The string must not be empty.")
        return None
    
    words = text.split(" ")
    reverse_words = words[::-1]
    
    palindromes = [word for word in words if word == word[::-1]]
        
    return " ".join(words + reverse_words), palindromes