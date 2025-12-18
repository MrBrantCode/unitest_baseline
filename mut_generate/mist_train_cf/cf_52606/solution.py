"""
QUESTION:
Write a function `process_list` that takes a list of elements as input, generates two new lists - one containing two times the integer values of the given list elements and another containing the squared integer values. The function should handle non-integer values by printing an error message and skipping those elements. The function should return both generated lists.
"""

def process_list(input_list):
    double_list = []
    squared_list = []
    for elem in input_list:
        try:
            val = int(elem)
            double_list.append(val*2)
            squared_list.append(val**2)
        except ValueError:
            print(f"Element {elem} is not a number and can't be processed.")
    return double_list, squared_list