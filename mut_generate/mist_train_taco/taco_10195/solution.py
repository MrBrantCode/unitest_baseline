"""
QUESTION:
Ms. E.T. came from planet Hex. She has 8 fingers in each hand which makes her count in hexadecimal way. When she meets you, she tells you that she came from 7E light years from the planet Earth. You see she means that it is 126 light years far away and she is telling you the numbers in hexadecimal. Now, you are in trouble to understand what those numbers really mean. Therefore, you have to convert the hexadecimal numbers to decimals.

Input:

First line of code contain T test cases.

every line of text case contain a Hex-value 

Output:

Every line of output contain a decimal conversion of given nunmber

Sample Input:

3

A

1A23

2C2A

Sample Output:

10

6691

11306
"""

def hex_to_decimal(hex_values):
    """
    Converts a list of hexadecimal strings to their corresponding decimal values.

    Parameters:
    hex_values (list of str): A list of hexadecimal strings to be converted.

    Returns:
    list of int: A list of integers representing the decimal conversions of the input hexadecimal strings.
    """
    return [int(hex_value, 16) for hex_value in hex_values]