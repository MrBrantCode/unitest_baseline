"""
QUESTION:
Write a function named `count_upper` that takes a string `s` as an argument and returns the number of uppercase vowels present in even indices of `s`. The function should consider the string indices starting from 0 as even. It should only count the vowels 'A', 'E', 'I', 'O', 'U'.
"""

def count_upper(s):
    # Define the uppercase vowels
    vowels = "AEIOU"

    count = 0

    # Iterate over string 's' at even indices
    for i in range(0, len(s), 2):
        # If s[i] is a vowel, increment the count
        if s[i] in vowels:
            count += 1

    # Return the count of uppercase vowels at even indices
    return count