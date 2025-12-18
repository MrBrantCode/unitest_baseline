"""
QUESTION:
Write a function `run_length_encoding` that takes a string of uppercase letters as input and returns the compressed version of the string using Run Length Encoding. The compressed string should consist of the count of consecutive characters followed by the character itself, unless the character appears only once consecutively, in which case it should not be followed by a count.
"""

def run_length_encoding(s):
    """
    This function takes a string of uppercase letters as input and returns the compressed version of the string using Run Length Encoding.

    :param s: A string of uppercase letters.
    :return: The compressed version of the string using Run Length Encoding.
    """
    
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize the count of consecutive characters to 1
    count = 1
    
    # If the string is empty, return the empty string
    if not s:
        return result
    
    # Iterate over the string starting from the second character
    for i in range(1, len(s)):
        # If the current character is equal to the previous character, increment the count
        if s[i] == s[i - 1]:
            count += 1
        # If the current character is not equal to the previous character, 
        # add the count and the previous character to the result string, then reset the count to 1
        else:
            if count > 1:
                result += str(count) + s[i - 1]
            else:
                result += s[i - 1]
            count = 1
    
    # Add the count and the last character to the result string
    if count > 1:
        result += str(count) + s[-1]
    else:
        result += s[-1]
    
    return result