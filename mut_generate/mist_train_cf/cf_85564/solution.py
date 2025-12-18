"""
QUESTION:
Create a function `check_parity(num)` that takes an integer `num` and returns whether it is "Even" or "Odd". Then, write a program that prompts the user for four integers: `start_range`, `end_range`, `total_numbers`, and `check_divisibility`, where `start_range` is less than `end_range`, `total_numbers` is greater than 0, and `check_divisibility` is greater than 0. The program should then generate `total_numbers` random integers between `start_range` and `end_range`, print each number along with whether it is even or odd, and count how many of these numbers are divisible by `check_divisibility`. Finally, print the count of divisible numbers. The program should handle invalid user inputs and unexpected errors.
"""

def check_parity(num):
    return "Even" if num % 2 == 0 else "Odd"