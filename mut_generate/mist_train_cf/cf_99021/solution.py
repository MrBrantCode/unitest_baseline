"""
QUESTION:
Write a function `check_all_alphabets(S)` that takes a string `S` as input and checks if it contains all the letters in the English alphabet. The function should return `True` if all alphabets are found and `False` otherwise. Additionally, if all alphabets are found, the function should also return a dictionary containing the frequency of each letter in the string. The function should be case-insensitive and ignore any non-alphabet characters in the string.
"""

import string
def check_all_alphabets(S):
    # convert string to lower case
    S = S.lower()
    
    # create a set of all alphabets
    alphabets = set(string.ascii_lowercase)
    
    # create a set of alphabets in the string
    found_alphabets = set(filter(lambda x: x in alphabets, S))
    
    # check if all alphabets are found
    if found_alphabets == alphabets:
        # calculate frequency of each letter
        freq = {}
        for letter in S:
            if letter.isalpha():
                if letter in freq:
                    freq[letter] += 1
                else:
                    freq[letter] = 1
        return True, freq
    else:
        return False, None