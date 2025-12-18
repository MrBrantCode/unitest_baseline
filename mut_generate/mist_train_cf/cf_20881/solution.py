"""
QUESTION:
Write a Python function to print the squares of all odd numbers in a given list. The function should use a while loop and a helper function called "is_odd" that determines if a number is odd using a bitwise operation (without the modulus operator). The "is_odd" function should take in a number and return True if it is odd and False if it is even.
"""

def print_odd_squares(nums):
    def is_odd(num):
        return num & 1 == 1

    i = 0
    while i < len(nums):
        if is_odd(nums[i]):
            print(nums[i] ** 2)
        i += 1