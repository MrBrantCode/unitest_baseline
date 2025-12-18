"""
QUESTION:
Write a function `generate_sorted_string` that takes a list of strings as input and returns a comma-separated string of the list's elements. The output string should be sorted in ascending order based on the length of each element in the list, and then alphabetically for elements of the same length. The function should not use the built-in string join method or any string manipulation functions, and it should not include any leading or trailing whitespace characters in the output string.
"""

def generate_sorted_string(strings):
    """
    Generate a comma-separated string of the input list's elements, 
    sorted in ascending order based on the length of each element, 
    and then alphabetically for elements of the same length.

    Args:
        strings (list): A list of strings.

    Returns:
        str: A comma-separated string of the input list's elements.
    """

    # Sort the list in ascending order based on the length of each element
    strings.sort(key=lambda x: (len(x), x))

    # Initialize an empty string
    output = ""

    # Iterate over each element in the sorted list
    for i in range(len(strings)):
        # Add the current element to the output string
        output += strings[i]
        
        # Add a comma if it's not the last element
        if i < len(strings) - 1:
            output += ","
            
    # Return the generated string without leading or trailing whitespace characters
    return output.strip()