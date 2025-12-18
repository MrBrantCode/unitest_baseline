"""
QUESTION:
Create a function named `create_new_array` that takes an array of integers as input. The function should return a new array containing only the odd numbers from the input array that are smaller than 5. The new array should not exceed a length of 5.
"""

def create_new_array(input_array):
    new_array = []
    count = 0
    
    for num in input_array:
        if num < 5 and num % 2 != 0 and count < 5:
            new_array.append(num)
            count += 1
    
    return new_array