"""
QUESTION:
Create a function `count_occurrences` that takes a string and a list of strings as parameters and returns a dictionary where the keys are the unique strings in the list and the values are the number of occurrences of each string. The input string is not required to be used in the function logic and can be ignored.
"""

def count_occurrences(string, string_list):
    # Initialize an empty dictionary
    occurrences = {}
    
    # Iterate over each string in the list
    for item in string_list:
        # Check if the string is already a key in the dictionary
        if item in occurrences:
            # If yes, increment the value by 1
            occurrences[item] += 1
        else:
            # If no, add the string as a new key with value 1
            occurrences[item] = 1
    
    return occurrences