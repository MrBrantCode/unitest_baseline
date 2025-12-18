"""
QUESTION:
Write a function `check_divisibility` that takes a list of integers as input and returns a list of boolean values. The function should check each number in the input list to see if it is divisible by 3 and return True if it is, and False otherwise. The input list must contain at least 5 numbers, and each number must be between 1 and 1000 (inclusive). If the input list is empty or does not meet these criteria, the function should print an error message and return.
"""

def check_divisibility(numbers):
    if not numbers:
        print("Error: Input list is empty.")
        return

    if len(numbers) < 5:
        print("Error: Input list should contain at least 5 numbers.")
        return

    divisible_by_3 = []
    for num in numbers:
        if 1 <= num <= 1000:
            divisible_by_3.append(num % 3 == 0)
        else:
            print(f"Error: {num} is not between 1 and 1000 (inclusive).")
            return

    return divisible_by_3