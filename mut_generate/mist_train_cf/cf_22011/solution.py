"""
QUESTION:
Write a function `reduce_array(numbers)` that takes an array of numbers as input and returns a single number. The function should calculate the sum of all positive numbers in the array and the sum of all negative numbers, then return the difference between these two sums. If there are no positive numbers in the array, the function should return the sum of all negative numbers. If there are no negative numbers in the array, the function should return the sum of all positive numbers. The input array will always contain at least one number.
"""

def reduce_array(numbers):
    positive_sum = sum(num for num in numbers if num > 0)
    negative_sum = sum(num for num in numbers if num < 0)
    
    if positive_sum == 0:
        return negative_sum
    elif negative_sum == 0:
        return positive_sum
    else:
        return positive_sum - negative_sum