"""
QUESTION:
Create a function `process_binary_numbers` that takes a list of binary numbers as strings and returns a list of integers. The function should remove any duplicate binary numbers from the list, sort the list in ascending order, and convert each binary number to its decimal equivalent. The function should return a list containing the sorted decimal equivalents of the unique binary numbers from the input list. The input list will contain binary numbers as strings and the output list should contain decimal numbers as integers.
"""

from typing import List

def process_binary_numbers(binary_list: List[str]) -> List[int]:
    # Remove duplicates
    unique_binaries = list(set(binary_list))
    
    # Sort the unique binary numbers
    unique_binaries.sort()
    
    # Convert binary numbers to decimal equivalents
    decimal_equivalents = [int(binary, 2) for binary in unique_binaries]
    
    return decimal_equivalents