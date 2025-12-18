"""
QUESTION:
Create a function named `calculate_sum` that calculates the sum of all positive even numbers greater than 5 and less than or equal to 1000 in a given array, with the additional constraint that the sum should not be divisible by 3.
"""

def calculate_sum(arr):
    total = 0

    for num in arr:
        if num > 5 and num <= 1000 and num % 2 == 0:
            total += num

    if total % 3 == 0:
        largest_even_divisible_by_3 = (1000 // 6) * 6
        total -= largest_even_divisible_by_3

    return total