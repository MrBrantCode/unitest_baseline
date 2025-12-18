"""
QUESTION:
Generate a function named `generate_unique_5_digit_number` that creates a 5-digit number where each digit appears only once. The function should not use any built-in random number generation methods.
"""

def generate_unique_5_digit_number(seed):
    """Generate a 5-digit number where each digit appears only once."""
    digits = []
    seed_value = seed
    while len(digits) < 5:
        seed_value = (seed_value * 1103515245 + 12345) % 2**31
        digit = seed_value % 10
        if digit not in digits:
            digits.append(digit)
    return int("".join(map(str, digits)))