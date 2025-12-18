"""
QUESTION:
Create a function called `int_to_roman` that converts an integer to a Roman numeral. The function should take an integer as input and return the corresponding Roman numeral as a string. The input integer must be between 1 and 3999 (inclusive). If the input is not an integer or is outside this range, the function should return an error message.
"""

def int_to_roman(input_integer):
    """
    Converts an integer to Roman numeral
  
    :param int: Integer to convert
    """
    if not isinstance(input_integer, type(1)):
        return "Input must be an integer."
    if not 0 < input_integer < 4000:
        return "Input must be between 1 and 3999."
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = ""
    for i in range(len(ints)):
        count = int(input_integer / ints[i])
        result += nums[i] * count
        input_integer -= ints[i] * count
    return result