"""
QUESTION:
Write a Python function named `find_max`, `find_min`, `find_average`, `find_sum`, and `check_presence` to process a list of integers. The `find_max` function should return the maximum value in the list, the `find_min` function should return the minimum value in the list, the `find_average` function should return the average of the values in the list, the `find_sum` function should return the sum of all the values in the list, and the `check_presence` function should return a boolean indicating whether a specific number is present in the list. The input list and the operations to be performed should be specified through command-line arguments using the `argparse` module. The program should handle the command-line arguments and call the appropriate functions to perform the specified operations. The results of the operations should be displayed based on the command-line arguments provided.
"""

def find_max(nums):
    return max(nums)

def find_min(nums):
    return min(nums)

def find_average(nums):
    return sum(nums) / len(nums)

def find_sum(nums):
    return sum(nums)

def check_presence(nums, number):
    return number in nums