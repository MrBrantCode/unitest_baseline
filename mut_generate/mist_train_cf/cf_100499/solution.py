"""
QUESTION:
Write a function called `reverse_hello` that takes a string as input. The function should return the input string 'hello' reversed and a table containing the ASCII values of each character in the string and its binary equivalent. If the input is not a string containing the word 'hello', the function should return an error message.
"""

def reverse_hello(input_str):
    if not isinstance(input_str, str) or input_str != 'hello':
        return "Error: input must be a string containing 'hello'"
    
    reverse_str = input_str[::-1]
    ascii_table = []
    for char in input_str:
        ascii_table.append((char, ord(char), bin(ord(char))[2:].zfill(8)))
    
    return reverse_str, ascii_table