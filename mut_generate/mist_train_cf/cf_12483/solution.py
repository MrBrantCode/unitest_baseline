"""
QUESTION:
Write a function `find_numbers(n)` that finds all numbers from 1 to `n` (inclusive) that are divisible by 6 and also have the sum of their digits divisible by 3. The function should return a list of such numbers.
"""

def find_numbers(n):
    def sum_of_digits(num):
        # Function to calculate the sum of digits of a number
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        return sum

    result = []
    for num in range(1, n + 1):
        if num % 6 == 0 and sum_of_digits(num) % 3 == 0:
            result.append(num)
    return result