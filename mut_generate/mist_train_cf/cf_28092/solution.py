"""
QUESTION:
Create a function `find_max_number` that takes a positive integer as input and returns the maximum number that can be formed by rearranging its digits.
"""

def find_max_number(n):
    num_str = str(n)  
    sorted_digits = sorted(num_str, reverse=True)  
    max_num = int("".join(sorted_digits))  
    return max_num