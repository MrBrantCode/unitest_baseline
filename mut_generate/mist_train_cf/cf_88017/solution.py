"""
QUESTION:
Given an array of integers, write a function named `find_second_smallest_prime` to find the second smallest prime number and return it. If there is no second smallest prime number, return "No second smallest prime number". The function should handle arrays containing any number of integers.
"""

def find_second_smallest_prime(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    smallestPrime = float('inf')
    secondSmallestPrime = float('inf')
    count = 0

    for num in arr:
        if is_prime(num):
            if num < smallestPrime:
                secondSmallestPrime = smallestPrime
                smallestPrime = num
            elif num > smallestPrime and num < secondSmallestPrime:
                secondSmallestPrime = num
            count += 1
    
    if count < 2:
        return "No second smallest prime number"
    else:
        return secondSmallestPrime