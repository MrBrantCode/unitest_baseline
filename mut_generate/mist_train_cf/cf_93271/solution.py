"""
QUESTION:
Create a function named `check_pangram` that takes a string as input and returns a tuple containing a boolean indicating whether the string is a pangram and a dictionary with the count of each letter in the string. The function should consider only English alphabets and ignore case sensitivity. The input string may contain non-alphabetic characters.
"""

def check_pangram(string):
    # Convert the string to lowercase and remove any non-alphabetic characters
    string = ''.join(filter(str.isalpha, string.lower()))
    
    # Create a set of unique letters in the string
    unique_letters = set(string)
    
    # Check if the set of unique letters is equal to the set of all alphabets
    is_pangram = len(unique_letters) == 26
    
    # Initialize a dictionary to store the count of each letter
    letter_count = {}
    
    # Count the occurrences of each letter in the string
    for letter in string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    return is_pangram, letter_count