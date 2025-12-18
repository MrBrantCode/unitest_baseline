"""
QUESTION:
Create a function named `convert_to_binary` that takes a list of integers as input. The function should return a list of strings where each string is the binary representation of the corresponding integer in the input list. The binary representation should not include the '0b' prefix.
"""

def convert_to_binary(arr):
    binary_array = []
    for num in arr:
        binary_num = bin(num).replace("0b", "")
        binary_array.append(binary_num)
    return binary_array