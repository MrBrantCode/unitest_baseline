"""
QUESTION:
Write a function to calculate the total number of elements, the count of even numbers, and the count of odd numbers in a given list of integers. The function should take a list as input and print the total number of elements, the number of even numbers, and the number of odd numbers.
"""

def count_numbers(nums):
    """
    Calculate the total number of elements, the count of even numbers, 
    and the count of odd numbers in a given list of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        tuple: A tuple containing the total number of elements, 
               the number of even numbers, and the number of odd numbers.
    """
    even_count = 0
    odd_count = 0

    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return len(nums), even_count, odd_count