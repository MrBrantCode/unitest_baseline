"""
QUESTION:
Write a function named `second_highest_even_element` that takes a list of integers as input and returns a tuple containing the second highest even number and the mean of all even numbers in the list. The function should handle both positive and negative numbers, and raise a custom exception if there are less than two even numbers in the list. The function should not use any pre-existing functions for calculating the mean or finding the second highest even number.
"""

class NotEnoughEvenNumbersException(Exception):
    def __init__(self):
        super().__init__("There are less than two even numbers in the list")

def second_highest_even_element(l: list):
    max1, max2 = None, None
    even_count = even_sum = 0
    for x in l:
        # Look only for even numbers
        if x % 2 == 0:
            even_count += 1
            even_sum += x
            if max1 is None or x > max1:
                max2 = max1
                max1 = x
            elif max2 is None or x > max2 and x != max1:
                max2 = x
            
    # Raise an exception if there aren't at least two even numbers
    if even_count < 2:
        raise NotEnoughEvenNumbersException()
    
    # Calculate the mean of all even numbers
    average = even_sum / even_count

    # Return a tuple containing the second highest even number and average
    return max2, average