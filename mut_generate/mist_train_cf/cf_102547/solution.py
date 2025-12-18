"""
QUESTION:
Create a function named `check_divisibility` that takes a list of integers as input. The function should check if each number in the list is divisible by 3 and return a list containing True if the number is divisible by 3 and False otherwise. The input list must contain at least 5 numbers, each between 1 and 1000 (inclusive). If the input list is empty or contains less than 5 numbers, or if any number is outside the specified range, the function should return an error message.
"""

def check_divisibility(numbers):
    if not numbers:
        return "Error: Input list is empty."

    if len(numbers) < 5:
        return "Error: Input list should contain at least 5 numbers."

    divisible_by_3 = []
    for num in numbers:
        if 1 <= num <= 1000:
            divisible_by_3.append(num % 3 == 0)
        else:
            return f"Error: {num} is not between 1 and 1000 (inclusive)."
    return divisible_by_3