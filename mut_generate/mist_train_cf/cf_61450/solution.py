"""
QUESTION:
Create a function `binary_to_octal(binary_num)` that takes an integer `binary_num` as input and returns its equivalent octal value as a string. The input `binary_num` is assumed to be a binary number and should be validated before conversion. If the input is not a valid binary number, the function should return an error message "Error! Invalid binary number." The function should also handle any exceptions that may occur during execution and return an error message with the exception details.
"""

def binary_to_octal(binary_num):
    try:
        bin_num = str(binary_num)
        if all([digit == '1' or digit == '0' for digit in bin_num]):
            dec_num = int(bin_num, 2)
            oct_num = oct(dec_num)
            return oct_num[2:]
        else:
            return "Error! Invalid binary number."
    except Exception as e:
        return "Error! " + str(e)