"""
QUESTION:
Write a function named find_divisible_numbers that takes an array of integers as input and returns the sum of the smallest and largest positive numbers that are divisible by 3. The function should ignore any negative numbers in the array. If the array does not contain any positive numbers divisible by 3, the function should return -1.
"""

def find_divisible_numbers(numbers):
    # Find all positive numbers divisible by 3
    divisible_numbers = [num for num in numbers if num > 0 and num % 3 == 0]
    
    # If no positive numbers divisible by 3, return -1
    if len(divisible_numbers) == 0:
        return -1
    
    # Find the smallest and largest numbers divisible by 3
    smallest_number = min(divisible_numbers)
    largest_number = max(divisible_numbers)
    
    # Return the sum of the smallest and largest numbers divisible by 3
    return smallest_number + largest_number