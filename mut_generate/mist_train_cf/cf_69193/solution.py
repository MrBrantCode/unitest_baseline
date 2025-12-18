"""
QUESTION:
Write a function `find_palindromic_substrings` that determines the frequency of specific palindromic substrings of length greater than 2 within a given string. Consider overlapping conditions in the search. The function should return a dictionary where keys are palindromic substrings and values are their frequencies.
"""

def find_palindromic_substrings(text):
    """
    This function determines the frequency of specific palindromic substrings of length greater than 2 within a given string.
    
    Parameters:
    text (str): The input string to search for palindromic substrings.
    
    Returns:
    dict: A dictionary where keys are palindromic substrings and values are their frequencies.
    """
    
    palindromes = {}
    
    for i in range(len(text)):
        for j in range(i+3, len(text)+1):
            substring = text[i:j]
            if substring == substring[::-1]: # check if the substring is a palindrome
                if substring in palindromes:
                    palindromes[substring] += 1
                else:
                    palindromes[substring] = 1
                    
    return palindromes