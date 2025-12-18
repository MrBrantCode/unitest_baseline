"""
QUESTION:
Write a function `reverse_and_format` that takes a list of integers as input, removes duplicates, reverses the list, and returns a string representation of the integers separated by semicolons and enclosed within square brackets. The input list should contain a minimum of 5 and a maximum of 20 integers. The function should handle negative numbers and floating-point numbers.
"""

def reverse_and_format(lst):
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.reverse()  # Reverse the list
    str_lst = [str(num) for num in unique_lst]  # Convert all numbers to strings
    result = ';'.join(str_lst)  # Join the strings with semicolons
    return '[' + result + ']'  # Enclose the result in square brackets