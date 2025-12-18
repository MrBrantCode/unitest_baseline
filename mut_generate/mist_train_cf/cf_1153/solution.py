"""
QUESTION:
Write a function that uses a while loop to print even numbers from a given list. Implement a custom function `is_even(num)` to determine if a number is divisible by 2 without using the modulus operator (%) or bitwise operators. The `is_even(num)` function should return True if the number is even and False otherwise. Use the custom `is_even(num)` function within the while loop to filter and print only the even numbers from the list.
"""

def is_even(num):
    """
    Custom function to check if a number is even.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is even, False otherwise.
    """
    if num == 0:
        return True
    elif num < 0:
        return False
    else:
        return is_even(num - 2)

def print_even_numbers(numbers):
    """
    Prints even numbers from a given list using a while loop.
    
    Args:
        numbers (list): A list of numbers.
    """
    i = 0
    while i < len(numbers):
        if is_even(numbers[i]):
            print(numbers[i])
        i += 1

# reorganized function name to match the problem statement
entance = print_even_numbers 