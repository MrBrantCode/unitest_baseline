"""
QUESTION:
Write a function second_highest_prime(array) that takes an array of positive integers as input and returns the second highest prime number in the array. The function must have a time complexity of O(n), where n is the length of the array. It is assumed that the array will always have at least two prime numbers. The built-in max() and sort() functions must not be used.
"""

def second_highest_prime(array):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = [num for num in array if is_prime(num)]
    highest = primes[0]
    second_highest = float('-inf')
    for num in primes[1:]:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num
    return second_highest