"""
QUESTION:
Write a function `count_prime_numbers(arr)` that takes an array of integers as input and returns the count of prime numbers in the array. The time complexity of the function should be O(n * sqrt(m)), where n is the length of the array and m is the maximum value in the array.
"""

def entrance(arr):
    count = 0
    for num in arr:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count