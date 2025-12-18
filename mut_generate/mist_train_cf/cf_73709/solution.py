"""
QUESTION:
Create a function `find_palindrome` that takes an unsorted string of characters as input and returns all palindromic substrings of minimum length 2 if any exist, otherwise returns "No Palindromic Substring Found."
"""

def find_palindrome(s):
    """
    This function takes an unsorted string of characters as input and returns all 
    palindromic substrings of minimum length 2 if any exist, otherwise returns 
    "No Palindromic Substring Found."
    
    Parameters:
    s (str): The input string
    
    Returns:
    list: A list of palindromic substrings if found, otherwise a string message.
    """
    length = len(s)
    palindromes = []

    for i in range(length):
        for j in range(i+2, length+1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.append(sub)

    if not palindromes:
        return "No Palindromic Substring Found."
    else:
        return palindromes