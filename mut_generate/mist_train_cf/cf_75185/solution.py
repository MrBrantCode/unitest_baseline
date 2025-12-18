"""
QUESTION:
Create a function `generate_dispersion_table` that takes an array of integers as input and returns a dictionary where the keys are the unique integers in the array and the values are their corresponding frequencies.
"""

def generate_dispersion_table(input_array):
    table = {}
    for num in input_array:
        if num in table:
            table[num] += 1
        else:
            table[num] = 1
    return table