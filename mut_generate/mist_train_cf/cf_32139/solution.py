"""
QUESTION:
Implement the `remove_even_numbers` function, which takes a list of integers as input and returns a new list with all even numbers removed. The function should also print the removed even numbers in the format "Removed: num1, num2, ...". Ensure the function does not modify the original input list.
"""

def remove_even_numbers(nums):
    removed = [num for num in nums if num % 2 == 0]
    print("Removed: ", ", ".join(map(str, removed)))
    return [num for num in nums if num % 2 != 0]