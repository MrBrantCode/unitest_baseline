"""
QUESTION:
Create a function called `string_manipulation` that takes two strings and an integer as parameters. The function should return a string that is a result of concatenating the two input strings, with the first string reversed and the second string repeated based on the value of the numeric parameter. The function should also handle errors when the numeric value is not positive, or when the input parameters are not in the correct format (i.e., the first two parameters are not strings or the third parameter is not an integer).
"""

def entrance(str1, str2, num):
    """
    Function to concatenate two strings with modifications and a numeric parameter.

    :param str1: First string input
    :type str1: str
    :param str2: Second string input
    :type str2: str
    :param num: Numeric value to repeat str2
    :type num: int
    
    :return: Concatenated string of str1 reversed and str2 repeated num times
    :rtype: str
    """

    # Error handling
    if not isinstance(str1, str):
        return 'Error: The first input should be a string.'
    if not isinstance(str2, str):
        return 'Error: The second input should be a string.'
    if not isinstance(num, int):
        return 'Error: The third input should be a number.'
    if num <= 0:
        return 'Error: The numeric value should be greater than zero.'

    # Reverse the first string
    str1 = str1[::-1]

    # Repeat the second string
    str2 = str2 * num

    return str1 + str2