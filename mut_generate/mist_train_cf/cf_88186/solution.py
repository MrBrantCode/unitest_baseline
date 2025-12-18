"""
QUESTION:
Implement a function named `handle_edge_cases` that takes a float `num` within the range of -1000 to 1000, rounds it to the nearest integer, and returns its binary equivalent as a string. The function should handle edge cases such as negative numbers and float inputs with decimal places beyond the standard 16 decimal places of precision, and should return "Number out of range!" if the input is outside the specified range. You cannot use any built-in functions or libraries to perform the rounding or conversion to binary.
"""

def handle_edge_cases(num):
    if num < -1000 or num > 1000:
        return "Number out of range!"
    
    if num >= 0:
        integer_part = int(num + 0.5)
    else:
        integer_part = int(num - 0.5)
    
    binary = ''
    num = abs(integer_part)
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    
    if integer_part < 0:
        binary = '-' + binary
    
    return binary