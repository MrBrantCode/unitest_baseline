"""
QUESTION:
Create a function `divisible_numbers` that takes two arrays as input: `numbers` and `divisors`, where `numbers` is an array of integers and `divisors` is an array of divisors. The function should return a dictionary where keys are the divisors and values are lists of elements from the `numbers` array that are divisible by the corresponding key divisor. Elements that are divisible by multiple divisors should appear in each corresponding list.
"""

def divisible_numbers(numbers, divisors):
    result = {}
    for divisor in divisors:
        result[divisor] = [num for num in numbers if num % divisor == 0]
    return result