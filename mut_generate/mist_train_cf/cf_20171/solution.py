"""
QUESTION:
Create a function called `separate_numbers` that takes an array of integers as input and returns four lists: prime numbers, even numbers, odd numbers, and numbers divisible by 3. The prime numbers list should be sorted in descending order, while the even numbers, odd numbers, and numbers divisible by 3 lists should be sorted in ascending order.
"""

def separate_numbers(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_numbers = sorted([num for num in nums if is_prime(num)], reverse=True)
    even_numbers = sorted([num for num in nums if num % 2 == 0])
    odd_numbers = sorted([num for num in nums if num % 2 != 0])
    divisible_by_3 = sorted([num for num in nums if num % 3 == 0])

    return prime_numbers, even_numbers, odd_numbers, divisible_by_3