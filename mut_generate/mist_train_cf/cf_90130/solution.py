"""
QUESTION:
Implement the function `findSmallestOddPrimeIndex(arr)` that finds the index of the smallest odd prime number in a given array of positive integers. The function should return the index of the smallest odd prime number. The time complexity should be O(n), where n is the number of elements in the array, and the space complexity should be O(1), using minimal additional space. Assume the array will always contain at least one odd prime number.
"""

import math

def findSmallestOddPrimeIndex(arr):
    def isOddPrime(num):
        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num))+1, 2):
            if num % i == 0:
                return False
        return True

    smallestOddPrimeIndex = -1
    for i in range(len(arr)):
        if isOddPrime(arr[i]):
            if smallestOddPrimeIndex == -1:
                smallestOddPrimeIndex = i
            else:
                if arr[i] < arr[smallestOddPrimeIndex]:
                    smallestOddPrimeIndex = i
    return smallestOddPrimeIndex