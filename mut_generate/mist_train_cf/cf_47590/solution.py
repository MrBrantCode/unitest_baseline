"""
QUESTION:
Write a function `bin_list_to_oct` that converts a list of positive binary numbers to their equivalent octal values and returns them in a dictionary, where each binary number is a key and its equivalent octal value is a value. The function should handle invalid inputs (non-binary numbers) by skipping them and continuing to process the rest of the list. The function should take a list of integers as input and return a dictionary.
"""

def bin_list_to_oct(bin_list):
    """
    Converts a list of binary numbers to their octal representations

    Args:
    bin_list: the list of binary numbers

    Returns:
    a dictionary where the keys are the binary numbers and the values are their octal representations.
    """
    conversion_dictionary = {}
    for binary in bin_list:
        if not str(binary).isnumeric() or not set(str(binary)).issubset('10'):
            continue

        decimal = int(str(binary), 2)
        octal = oct(decimal).replace("0o", "")
        conversion_dictionary[binary] = octal
    return conversion_dictionary