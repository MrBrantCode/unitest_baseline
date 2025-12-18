"""
QUESTION:
Implement a function `count_leading_zeros` that takes a list of binary numbers as strings and a custom progress bar message as input, and returns a list containing the count of leading zeros for each binary number. The function should display a progress bar using the `tqdm` library with the provided custom message. The input list will only contain binary numbers (strings consisting of '0's and '1's).
"""

from typing import List
from tqdm import tqdm

def count_leading_zeros(binary_numbers: List[str], pbar_msg: str) -> List[int]:
    leading_zeros_count = []
    for binary_num in tqdm(binary_numbers, desc=pbar_msg):
        leading_zeros = 0
        for bit in binary_num:
            if bit == '0':
                leading_zeros += 1
            else:
                break
        leading_zeros_count.append(leading_zeros)
    return leading_zeros_count