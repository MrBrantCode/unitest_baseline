"""
QUESTION:
Write a function called `binaryToDecimal` that takes a binary number as input and returns its decimal equivalent. The binary number is represented as a decimal integer (e.g. 1010 is represented as 1010, not '1010').
"""

def binaryToDecimal(binary): 
    decimal, i = 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i = i + 1
    return decimal