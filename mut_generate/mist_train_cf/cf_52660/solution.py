"""
QUESTION:
Write a function named `sum_ascii_lower` that takes a string `s` as input and returns a tuple containing two values. The first value is the count of lowercase consonants found at odd index positions in the string, and the second value is the sum of their ASCII values. Assume that the indexing of the string starts from 0, so the first character is at an even index and the second character is at an odd index.
"""

def sum_ascii_lower(s):
    # Define a list of lowercase consonants
    consonants = list('bcdfghjklmnpqrstvwxyz')
    
    # Initialize count and sum variable
    count, sum_ascii = 0, 0
    
    # Loop through string characters in odd index positions
    for i in range(1, len(s), 2):
        # If character is a lower case consonant
        if s[i] in consonants:
            count += 1
            sum_ascii += ord(s[i])
            
    return count, sum_ascii