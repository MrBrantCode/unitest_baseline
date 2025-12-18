"""
QUESTION:
Create a function called `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should remove any duplicates from the original list before checking for prime numbers. The time complexity of the function should be O(n^2) and the space complexity should be O(n).
"""

def get_prime_numbers(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    unique_nums = set(nums)
    return [num for num in unique_nums if is_prime(num)]