"""
QUESTION:
Create a function named `vowel_counter` that takes a string `term` as input. The function should count the frequency of each vowel in the term, ignoring case and non-alphabetic characters. If the term is formed entirely of vowels, return a dictionary with each vowel and its frequency. Otherwise, return a message stating that the term is not formed entirely of vowels.
"""

def vowel_counter(term):
    """
    This function takes a string term as input, counts the frequency of each vowel 
    in the term (ignoring case and non-alphabetic characters), and returns a 
    dictionary with each vowel and its frequency if the term is formed entirely 
    of vowels. Otherwise, it returns a message stating that the term is not 
    formed entirely of vowels.
    
    Parameters:
    term (str): The input string
    
    Returns:
    dict or str: A dictionary with vowel frequencies or an error message
    """
    
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Filter non-alphabetic characters and convert to lower case
    filtered_term = ''.join(filter(str.isalpha, term.lower()))
    
    for ch in filtered_term:
        if ch in vowels.keys():
            vowels[ch] += 1
            
    if sum(vowels.values()) == len(filtered_term):
        return vowels
    else:
        return "The term is not formed entirely of vowels."