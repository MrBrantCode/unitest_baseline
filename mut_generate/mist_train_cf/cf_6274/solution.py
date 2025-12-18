"""
QUESTION:
Write a function to print the squares of odd numbers in a given list. The function should use a while loop and a separate function called "is_odd" to determine if a number is odd or even using a bitwise operation. The function should not use the modulus operator (%) to check for odd or even numbers.
"""

def print_odd_squares(nums):
    def is_odd(num):
        return num & 1 == 1
    
    i = 0
    while i < len(nums):
        if is_odd(nums[i]):
            print(nums[i] ** 2)
        i += 1