"""
QUESTION:
Write a function named `decimal_to_binary` that takes an integer as input and returns its binary representation as a string. The function should not use any built-in functions or libraries for number conversion. If the input is 0, the function should return "0".
"""

def decimal_to_binary(decimal):
    binary = ""
    
    if decimal == 0:
        binary = "0"
    
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    
    return binary