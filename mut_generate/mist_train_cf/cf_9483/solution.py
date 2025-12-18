"""
QUESTION:
Create a function named `convert_to_dictionary` that takes a list of strings as input and returns a dictionary. The keys in the dictionary should be numbers in ascending order starting from 1, and the values should be strings in uppercase letters. The function should only include strings that have at least 3 characters and contain at least one vowel in the resulting dictionary.
"""

def convert_to_dictionary(lst):
    vowels = ['A', 'E', 'I', 'O', 'U']  # List of vowels
    result = {}  # Empty dictionary to store the result
    count = 1  # Starting number for keys
    
    for string in lst:
        # Check if the string has at least 3 characters and contains at least one vowel
        if len(string) >= 3 and any(vowel in string.upper() for vowel in vowels):
            result[count] = string.upper()  # Assign the string in uppercase as value
            count += 1  # Increment the key value
            
    return result