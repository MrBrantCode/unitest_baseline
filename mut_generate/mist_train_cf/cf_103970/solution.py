"""
QUESTION:
Create a function `find_two_largest_numbers` that takes an array of integers as input and returns the two largest numbers in ascending order. The function should iterate through the array only once.
"""

def find_two_largest_numbers(array):
    largest1 = float('-inf')
    largest2 = float('-inf')
    
    for num in array:
        if num > largest1:
            largest2 = largest1
            largest1 = num
        elif num > largest2:
            largest2 = num
    
    return [largest2, largest1]