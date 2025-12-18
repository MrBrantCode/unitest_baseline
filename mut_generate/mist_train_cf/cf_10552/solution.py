"""
QUESTION:
Write a function named `max_pairwise_product` that takes an array of integers as input and returns the maximum product of any two numbers in the array. The function must have a time complexity of O(n), where n is the length of the array. The input array must have at least two elements.
"""

def max_pairwise_product(numbers):
    max_num = second_max_num = float('-inf')

    for num in numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num

    return max_num * second_max_num