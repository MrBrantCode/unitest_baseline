"""
QUESTION:
Create a function `convert_list_elements` that takes a list of integers as input, removes any duplicates, converts all odd numbers greater than 10 to strings, and all even numbers less than or equal to 10 to floats, while maintaining the original order of elements. The function should return the resulting list.
"""

def convert_list_elements(lst):
    # Remove duplicate elements
    unique_lst = list(dict.fromkeys(lst))

    # Convert odd numbers greater than 10 to strings and even numbers less than or equal to 10 to floats
    result = [str(num) if num > 10 and num % 2 != 0 else float(num) if num <= 10 and num % 2 == 0 else num for num in unique_lst]

    return result