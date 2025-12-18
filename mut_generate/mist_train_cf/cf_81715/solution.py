"""
QUESTION:
Write a function base_conversion(input_num, input_base, output_base) that takes a number input_num in base input_base and returns the equivalent number in base output_base. The function should be able to convert from any base between 2 and 36 to any base between 2 and 36.
"""

def entrance(input_num, input_base, output_base):
    # Define a string of all possible digits
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Convert the input number from the input base to base 10
    temp_dec = 0
    power = 0
    for char in reversed(input_num):
        temp_dec += digits.index(char) * (input_base ** power)
        power += 1
    
    # Convert the decimal number to the output base
    if temp_dec == 0:
        return '0'
    
    output_num = ''
    while temp_dec > 0:
        output_num = digits[temp_dec % output_base] + output_num
        temp_dec //= output_base
    
    return output_num