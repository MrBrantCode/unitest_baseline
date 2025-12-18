"""
QUESTION:
Write a function `reversed_diff(num)` that calculates the absolute difference between an integer and its reverse. The function should handle negative integers and return "Overflow" if the reversed number exceeds the maximum integer limit. If the input is not an integer, return "Not an Integer".
"""

def reversed_diff(num):
    """
    Calculates the absolute difference between an integer and its reverse.
    
    Args:
    num (int): The input integer.

    Returns:
    int or str: The absolute difference if the input is a valid integer, "Overflow" if the reversed number exceeds the maximum integer limit, or "Not an Integer" if the input is not an integer.
    """
    if isinstance(num, int):
        # turn number into string for reversing
        str_num = str(abs(num))
        # reverse the string
        reversed_str_num = str_num[::-1]
        
        # check for integer overflow
        try:
            int(reversed_str_num)  # try to convert the reversed string into integer
        except ValueError:  # if conversion fails -> integer overflow condition
            return "Overflow"
        else:  # successful conversion
            # find absolute difference between original number & reversed number
            abs_diff = abs(num - int(reversed_str_num))
            return abs_diff
    else:
        return "Not an Integer"