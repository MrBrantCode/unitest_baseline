"""
QUESTION:
Create a function called `split_string` that takes a string and a delimiter as arguments and returns a list containing the string split by the delimiter. The function should remove any leading or trailing whitespace from each split element in the resulting list, as well as any other whitespace within the split elements. If the input string is empty or the delimiter is not found in the string, the function should return an empty list. The function should handle cases where the delimiter appears multiple times consecutively, at the beginning or end of the string, or is a substring of a word in the string.

Constraints:
- The input string will not exceed 10^6 characters.
- The delimiter will not exceed 10 characters.
- The input string will only contain printable ASCII characters.
"""

def split_string(string, delimiter):
    """
    This function splits a given string by a specified delimiter, removes leading/trailing 
    and extra whitespace from each part, and returns the result as a list of strings.

    Args:
    string (str): The input string to be split.
    delimiter (str): The delimiter used to split the string.

    Returns:
    list: A list of strings split by the delimiter with no leading/trailing or extra whitespace.
    """

    # Check if the string is empty or the delimiter is not found
    if not string or delimiter not in string:
        return []
    
    # Initialize the result list
    result = []
    
    # Split the string using the delimiter
    split_parts = string.split(delimiter)
    
    # Iterate through the split parts
    for part in split_parts:
        # Remove leading and trailing whitespace
        part = part.strip()
        
        # Remove any other whitespace within the split element
        part = "".join(part.split())
        
        # Add the part to the result list if it is not empty
        if part:
            result.append(part)
    
    return result