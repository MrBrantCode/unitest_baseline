"""
QUESTION:
Create a function called `find_floats_and_ints` that takes a string as input and returns two separate lists, one containing integers and the other containing floating-point numbers found in the string. The function should not use any built-in or library functions for parsing numbers. The input string may contain positive numbers in decimal or integer form, but may also include non-numeric characters. Assume that the input string does not contain negative numbers or numbers in scientific notation.
"""

def find_floats_and_ints(input_string):
    float_list = []
    float_number = []
    int_list = []
    int_number = []

    for char in input_string:    
        if char.isdigit():
            if float_number:
                float_number.append(char)
            else:
                int_number.append(char)
                
        elif char == '.':
            if int_number:
                float_number.extend(int_number)
                int_number = []
            float_number.append(char)
        else:
            if float_number:
                float_list.append("".join(float_number))
                float_number = []
            elif int_number:
                int_list.append("".join(int_number))
                int_number = []

    if float_number:
        float_list.append("".join(float_number))
    elif int_number:
        int_list.append("".join(int_number))

    return [int(x) for x in int_list], [float(x) for x in float_list]