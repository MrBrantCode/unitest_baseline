"""
QUESTION:
Create a function `filter_odd_numbers` that takes an array of numbers as input and returns a new array containing only the odd numbers from the input array. The function should use the modulo operator to identify odd numbers, which are numbers that leave a remainder of 1 when divided by 2.
"""

def filter_odd_numbers(input_array):
    output_array = []
    for i in input_array:
        if i%2 == 1:
            output_array.append(i)
    return output_array