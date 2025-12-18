"""
QUESTION:
Write a function named `partition_list` that takes a list of integers as input and returns a pair of lists. The first list should contain the even numbers from the input list in ascending order, and the second list should contain the odd numbers from the input list in descending order. The function should remove any duplicate numbers from the input list before ordering them. The function should have a linear time complexity, or at least be efficient enough to handle large inputs.
"""

def partition_list(numbers):
    evens = sorted([num for num in set(numbers) if num % 2 == 0])
    odds = sorted([num for num in set(numbers) if num % 2 == 1], reverse=True)
    return [evens, odds]