"""
QUESTION:
Write a recursive function named `print_numbers` that takes an integer `current_number` and an optional integer `limit` (defaulting to 10) as arguments. The function should print numbers starting from `current_number` up to `limit`. Implement a base case to stop the recursion when `current_number` exceeds `limit`.
"""

def print_numbers(current_number, limit=10):
    if current_number > limit:
        return
    else:
        print(current_number)
        print_numbers(current_number + 1, limit)