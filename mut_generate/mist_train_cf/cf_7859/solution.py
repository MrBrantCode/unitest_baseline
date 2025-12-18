"""
QUESTION:
Write a function `findSmallestOddPrimeIndex(arr)` that finds the index of the smallest odd prime number in the given array of positive integers. The function should have a time complexity of O(n), where n is the number of elements in the array, and a space complexity of O(1). If the array does not contain any odd prime numbers, the function should return -1.
"""

import math

def findSmallestOddPrimeIndex(arr):
    smallestOddPrimeIndex = -1
    for i in range(len(arr)):
        if isOddPrime(arr[i]):
            if smallestOddPrimeIndex == -1:
                smallestOddPrimeIndex = i
            else:
                if arr[i] < arr[smallestOddPrimeIndex]:
                    smallestOddPrimeIndex = i
    return smallestOddPrimeIndex

def isOddPrime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True