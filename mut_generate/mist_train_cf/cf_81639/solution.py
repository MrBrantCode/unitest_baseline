"""
QUESTION:
Write a function named calc_total that calculates the total of all elements in a multidimensional list. The multidimensional list may contain both integers and string representations of integers. The function must handle string representations of integers and skip any strings that cannot be parsed to integers without crashing. The function should not use built-in functions or variable names that conflict with Python's built-in functions or variables.
"""

def calc_total(nested_list):
    total = 0
    for sublist in nested_list:
        for element in sublist:
            try:
                total += int(element)
            except ValueError:
                print(f'"{element}" cannot be parsed to an integer. Skipping...')
    return total