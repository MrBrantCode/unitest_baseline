"""
QUESTION:
Implement a function named `filter_long_strings` that takes a list of strings as input and returns a new list containing only the strings that have a length of 5 or more characters. The input list can have up to 1000 strings, each with up to 1000 characters. The output list should be sorted in alphabetical order.
"""

def filter_long_strings(strings):
    # Initialize an empty list to store the filtered strings
    filtered_strings = []
    
    # Iterate over each string in the input list
    for string in strings:
        # Check if the length of the string is greater than or equal to 5
        if len(string) >= 5:
            # If so, add it to the filtered_strings list
            filtered_strings.append(string)
    
    # Sort the filtered_strings list in alphabetical order
    filtered_strings.sort()
    
    # Return the filtered_strings list
    return filtered_strings