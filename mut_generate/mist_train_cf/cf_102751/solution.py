"""
QUESTION:
Write a function named 'count_elements' that takes a list as input and returns the total number of elements in the list without using the built-in len() function. Use a for loop to iterate over the list elements. The function should not take any additional parameters.
"""

def count_elements(input_list):
    count = 0
    for element in input_list:
        count += 1
    return count