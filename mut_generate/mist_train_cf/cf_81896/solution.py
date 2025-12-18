"""
QUESTION:
Write a recursive function `sum_multi_dimensional_array` that calculates the total sum of integers in a multidimensional array of any depth. The function should ignore non-integer elements and handle arrays containing both positive and negative integers.
"""

def sum_multi_dimensional_array(input_array):
    sum = 0
    for i in input_array:
        if type(i) == list:
            sum += sum_multi_dimensional_array(i)
        elif type(i) == int:
            sum += i
    return sum