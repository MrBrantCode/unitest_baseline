"""
QUESTION:
Write a function named `count_occurrences` that takes a string as input and returns a dictionary containing the count of each alphanumeric character in the string. The function should only use a for loop to iterate over the string and cannot use any built-in functions or data structures to count the occurrences.
"""

def count_occurrences(string):
    # Create an empty dictionary to store the occurrences
    occurrences = {}
    
    # Iterate over each character in the string
    for char in string:
        # Check if the character is alphanumeric
        if char.isalnum():
            # Check if the character is already in the dictionary
            if char in occurrences:
                # If it is, increment the count by 1
                occurrences[char] += 1
            else:
                # If it is not, add the character to the dictionary with a count of 1
                occurrences[char] = 1
    
    # Return the dictionary with the occurrences
    return occurrences