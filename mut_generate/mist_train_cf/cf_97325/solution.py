"""
QUESTION:
Write a function `calculate_even_sum_odd_average` that takes a list of integers as input and calculates the sum of all even numbers and the average of all odd numbers in the list. The function should only consider numbers within the range of 1 to 100 (inclusive) and exclude any numbers that are divisible by 5. The function should use a while loop for calculations.
"""

def calculate_even_sum_odd_average(numbers):
    """
    Calculate the sum of even numbers and average of odd numbers within the range of 1 to 100.
    
    Args:
        numbers (list): A list of integers.
    
    Returns:
        tuple: A tuple containing the sum of even numbers and the average of odd numbers.
    """

    sum_even = 0
    count_odd = 0
    sum_odd = 0

    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0 and 1 <= numbers[i] <= 100 and numbers[i] % 5 != 0:
            sum_even += numbers[i]
        elif numbers[i] % 2 != 0 and 1 <= numbers[i] <= 100 and numbers[i] % 5 != 0:
            count_odd += 1
            sum_odd += numbers[i]
        i += 1

    average_odd = sum_odd / count_odd if count_odd > 0 else 0

    return sum_even, average_odd