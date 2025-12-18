"""
QUESTION:
Create a function called `get_sorted_unique_even_numbers` that takes a list of integers as input and returns a new list containing only the unique even numbers from the input list, sorted in descending order. The returned list should not contain any duplicate numbers.
"""

def get_sorted_unique_even_numbers(nums):
    even_nums = [num for num in set(nums) if num % 2 == 0]
    even_nums.sort(reverse=True)
    return even_nums