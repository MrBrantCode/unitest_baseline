"""
QUESTION:
Write a function named `group_and_sort` that takes a list of positive integers as input, removes any duplicates, groups the numbers according to their last digit, and sorts each group in ascending order. The function should return a list of lists, where each inner list contains the numbers with the same last digit, sorted in ascending order.
"""

def group_and_sort(numbers):
    numbers = list(set(numbers))  # Remove duplicates from the list
    groups = [[] for _ in range(10)]  # Create a list of 10 empty lists for each digit

    for num in numbers:
        last_digit = num % 10
        groups[last_digit].append(num)

    for i in range(10):
        groups[i].sort()  # Sort each group in ascending order

    return [group for group in groups if group]