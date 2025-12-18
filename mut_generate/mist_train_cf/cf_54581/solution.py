"""
QUESTION:
Create a function `ascii_check` that accepts a list of strings and returns a list of strings. Each returned string should contain the count of ASCII characters in the corresponding input string. The count should be stated as "the number of ASCII characters is [count] in the string [index] of the input." where [count] is the actual number of ASCII characters and [index] is the 1-based index of the input string.
"""

def ascii_check(lst):
    """
    This function accepts a list of strings, returning a string indicating the count of ASCII characters in every individual string in the list. 
    Each response should be part of a list, stating "the number of ASCII characters in the i'th input string" - "i" should be replaced with the actual count of ASCII characters present.
    
    """
    result = []
    for i, string in enumerate(lst, 1):
        ascii_count = len([char for char in string if ord(char) < 128])
        result.append("the number of ASCII characters is {} in the string {} of the input.".format(ascii_count, i))
    return result