"""
QUESTION:
Write a function named `filter_and_sort` that takes a list of numbers as input and returns the following information:

- Filters the list to include only numbers that are divisible by both 3 and 5, sorts them in descending order, and calculates the product of these numbers.
- Finds the highest prime number in the filtered list, if any.

The function should handle the case where the input list is empty, and the time complexity should be O(n), where n is the length of the input list.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def filter_and_sort(numbers):
    filtered_numbers = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
    filtered_numbers.sort(reverse=True)
    product = 1
    highest_prime = None
    for num in filtered_numbers:
        product *= num
        if is_prime(num):
            if highest_prime is None or num > highest_prime:
                highest_prime = num
    return filtered_numbers, product, highest_prime