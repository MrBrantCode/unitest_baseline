"""
QUESTION:
Write a function named `binary_to_decimal` that takes a binary number as input and returns its decimal representation. The function should handle exceptions properly. Assume that the input is a valid binary number without the '0b' prefix.
"""

def binary_to_decimal(binary):
    try:
        binary = str(binary)
        decimal, i, n = 0, 0, 0
        while binary != '0': 
            dec = int(binary) % 10
            decimal = decimal + dec * pow(2, i) 
            binary = str(int(binary)//10)
            i += 1
        return decimal
    except Exception as e:
        print("An error occurred: ", e)