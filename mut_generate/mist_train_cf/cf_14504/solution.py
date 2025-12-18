"""
QUESTION:
Create a function named `check_pangram` that takes a string as input. The function should return a boolean value indicating whether the input string is a pangram (i.e., it contains all 26 letters of the English alphabet) and a dictionary containing the count of each letter in the string. The function should ignore case and non-alphabetic characters, considering only the English alphabet.
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