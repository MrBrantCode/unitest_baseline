"""
QUESTION:
Create a function named `count_occurrences` that takes a string `string` as input and returns a dictionary where the keys are the unique characters in the string and the values are the number of occurrences of each character. The input string should only contain lowercase alphabets and have a length between 1 and 1000 characters. The function should not use any built-in Python functions or libraries for counting occurrences or creating dictionaries.
"""

def count_occurrences(string):
    # Initialize an empty dictionary to store the occurrences
    occurrences = {}
    
    # Iterate through each character in the string
    for char in string:
        # If the character is already a key in the dictionary, increment its value by 1
        if char in occurrences:
            occurrences[char] += 1
        # If the character is not a key in the dictionary, add it with a value of 1
        else:
            occurrences[char] = 1
    
    return occurrences