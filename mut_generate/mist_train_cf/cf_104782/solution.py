"""
QUESTION:
Create a function named `convert_to_binary` that takes a list of integers as input and returns a list of strings containing their binary representations. The input list should not exceed a length of 100, and each integer should be between 0 and 1000 (inclusive). If these conditions are not met, the function should return an error message.
"""

def convert_to_binary(nums):
    if len(nums) > 100:
        return "Error: Maximum length of list should be 100."
    binary_list = []
    for num in nums:
        if num < 0 or num > 1000:
            return "Error: Each integer should be between 0 and 1000 (inclusive)."
        binary = bin(num)[2:]
        binary_list.append(binary)
    return binary_list