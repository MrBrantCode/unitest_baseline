"""
QUESTION:
Given an array of integers and a target number, write a function `countPrimeOccurrences` that returns the number of occurrences of the target number in the array, but only consider the numbers that are greater than or equal to zero and are prime numbers. The function should have a time complexity of O(n), where n is the length of the array.
"""

def countPrimeOccurrences(arr, target):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for num in arr:
        if num >= 0 and is_prime(num) and num == target:
            count += 1
    return count