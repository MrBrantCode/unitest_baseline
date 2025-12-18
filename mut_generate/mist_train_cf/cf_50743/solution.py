"""
QUESTION:
Create a function `find_unique_elements` that takes a string input and returns a dictionary where each key is a unique alphabetical character from the string and its corresponding value is a list of indices where the character appears in the string. The function should handle non-string input types by returning an error message. The function should be case-sensitive.
"""

def find_unique_elements(str_input):
    # Confirm the input is a string
    try:
        assert type(str_input) == str
    except AssertionError:
        return "Error: Input is not a string."

    unique_elements = {}

    # Iterate through the string
    for i, j in enumerate(str_input):
        # If the character is not in the dictionary, add it
        if j not in unique_elements.keys():

            # Add character to dictionary and start their index list
            unique_elements[j] = [i] 
        else:
            # If the character is already in the dictionary, append
            # new index to their index list
            unique_elements[j].append(i)

    return unique_elements