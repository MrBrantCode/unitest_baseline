"""
QUESTION:
Create a function named `even_numbers` that takes a list of mixed data types as input and returns a new list containing only the even numbers (integers and floats) from the original list, sorted in descending order. The function should ignore non-numeric values and include both integers and floats in the output.
"""

def even_numbers(lst):
    even_lst = [item for item in lst if isinstance(item, (int, float)) and item % 2 == 0]
    even_lst.sort(reverse=True)
    return even_lst