"""
QUESTION:
Create a function `find_known_palin(string, known_palin)` that takes two parameters: a string of characters and a list of known palindromes. The function should return the second last occurrence of any palindrome from the known palindromes list found in the input string. If no palindromes are found, return an empty list.
"""

def find_known_palin(string, known_palin):
    """
    This function takes a string and a list of known palindromes, 
    and returns the second last occurrence of any palindrome from the known palindromes list found in the input string.
    
    Parameters:
    string (str): The input string.
    known_palin (list): A list of known palindromes.
    
    Returns:
    str: The second last occurrence of any palindrome from the known palindromes list found in the input string. 
         If no palindromes are found, returns an empty list.
    """
    result = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            word = string[i:j + 1]
            if word in known_palin:
                result.append(word)
    return result if not result else result[-2]