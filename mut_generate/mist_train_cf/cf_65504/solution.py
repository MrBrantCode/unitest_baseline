"""
QUESTION:
Write a function `segregate_sort(nums)` that takes an integer array `nums` as input and returns three sorted lists: even numbers, odd numbers, and prime numbers. Note that prime numbers should not be included in the even or odd categories if they are even or odd.
"""

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    return False

def segregate_sort(nums):
    primes, even, odd = [], [], []
    for num in nums:
        if is_prime(num):
            primes.append(num)
        elif num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return sorted(even), sorted(odd), sorted(primes)