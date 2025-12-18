"""
QUESTION:
Write a function named `count_lower_unique` that calculates the number of unique lowercase consonants at odd indices in a string, excluding the first and the last character. The function should not count any repeating consonants.
"""

def count_lower_unique(s):
    # define a list of lowercase consonants
    lowercase_consonants = 'bcdfghjklmnpqrstvwxyz'
    
    # create a set to store unique consonants
    unique_consonants = set()
    
    # check every odd-indexed character excluding the first and the last
    for i in range(2, len(s) - 1, 2):
        
        # if the character is a lowercase consonant, add it to the set
        if s[i] in lowercase_consonants:
            unique_consonants.add(s[i])
            
    # return the size of the set
    return len(unique_consonants)