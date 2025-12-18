"""
QUESTION:
Write a function named `filter_numbers` that takes a list of integers and non-integer values as input. The function should filter out numbers that are divisible by both 3 and 5 but not by 2, and return their sum. If the input list is empty or no numbers meet the filtering criteria, the function should print "No numbers to filter."
"""

def filter_numbers(numbers):
    filtered_numbers = [num for num in numbers if isinstance(num, int) and num % 3 == 0 and num % 5 == 0 and num % 2 != 0]
    return sum(filtered_numbers) if filtered_numbers else None