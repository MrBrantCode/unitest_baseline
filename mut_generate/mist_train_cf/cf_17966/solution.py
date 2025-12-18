"""
QUESTION:
Create a function named `filter_numbers` that takes three parameters: a list of numbers, a threshold number, and a prime number. This function should return a new list containing numbers from the original list that are greater than the threshold and divisible by the prime number, without any duplicates. The function should achieve this with a time complexity of O(n) and space complexity of O(n).
"""

def filter_numbers(numbers, threshold, prime_number):
    result = set(num for num in numbers if num > threshold and num % prime_number == 0)
    return list(result)