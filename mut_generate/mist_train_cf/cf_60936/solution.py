"""
QUESTION:
Write a function `kth_smallest_prime(array, k)` that finds the kth smallest prime number in the given array. The function should return the kth smallest prime number if it exists, otherwise return -1. The array may contain duplicate values and the input size may be large. Note that a prime number is a number greater than 1 whose only factors are 1 and the number itself.
"""

def kth_smallest_prime(array, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                return False
        return True

    primeArr = []
    for num in array:
        if is_prime(num):
            primeArr.append(num)
    primeArr.sort()
    if k <= len(primeArr):
        return primeArr[k - 1]  
    return -1