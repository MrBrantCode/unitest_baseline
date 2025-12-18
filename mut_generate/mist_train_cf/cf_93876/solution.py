"""
QUESTION:
Write a function named `sum_of_digits` that takes a positive integer `n` as input and returns the sum of the digits in `n` excluding any digits that are divisible by 3. The function should have a time complexity of O(m), where m is the number of digits in `n`.
"""

def sum_of_digits(n):
    # Initialize sum
    sum = 0

    # Convert the number to string
    num_str = str(n)

    # Iterate through each character in the string
    for char in num_str:
        # Convert character to integer
        digit = int(char)

        # If digit is not divisible by 3, add it to the sum
        if digit % 3 != 0:
            sum += digit

    return sum