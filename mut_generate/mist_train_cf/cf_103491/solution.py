"""
QUESTION:
Create a function `count_and_sum_elements` that takes an array of integers and an integer `x` as input, and returns a tuple containing the count of all elements in the array that are larger than `x` and their sum.
"""

def count_and_sum_elements(array, x):
    count = 0
    sum_of_elements = 0
    
    for element in array:
        if element > x:
            count += 1
            sum_of_elements += element
    
    return count, sum_of_elements