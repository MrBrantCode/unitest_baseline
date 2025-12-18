"""
QUESTION:
Write a function `get_all_palindromes` that finds all substrings in a given string that are palindromes. A palindrome is a string that reads the same backward as forward. The function should return a list of all palindromic substrings found in the input string. The input string will only contain lowercase letters.
"""

def get_all_palindromes(input_string):
    """
    Finds all substrings in a given string that are palindromes.
    
    Args:
        input_string (str): The input string to find palindromes in.
    
    Returns:
        list: A list of all palindromic substrings found in the input string.
    """
    palindromes = []
    for substring_length in range(1, len(input_string) + 1):
        for i in range(len(input_string) - substring_length + 1):
            sub_string = input_string[i: i + substring_length]
            if sub_string == sub_string[::-1]:
                palindromes.append(sub_string)
    return palindromes