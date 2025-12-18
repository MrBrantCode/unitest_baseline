"""
QUESTION:
Create a function called `count_vowels` that takes a string `s` as input and returns a dictionary with the frequency of each vowel in the string. The function should handle both lowercase and uppercase vowels separately and exclude any vowels that do not appear in the string.
"""

def count_vowels(s):
    # Define vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
  
    # Create a dictionary
    frequency = {i: 0 for i in vowels}

    # Count vowels
    for char in s:
        if char in vowels:
            frequency[char] += 1

    # Filter out vowels that did not occur in the string
    frequency = {k: v for k,v in frequency.items() if v>0}

    return frequency