"""
QUESTION:
Create a function `findSecondSmallestOddPrimeGreaterThan100` that takes an array of positive integers as input and returns the second smallest odd prime number greater than 100 in the array. The array is guaranteed to contain at least one prime number greater than 100.
"""

def isOddPrimeGreaterThan100(number):
    if number <= 100 or number % 2 == 0:  
        return False
    for i in range(3, int(number**0.5) + 1, 2):  
        if number % i == 0:
            return False
    return True

def findSecondSmallestOddPrimeGreaterThan100(array):
    smallest = secondSmallest = float('inf')
    for number in array:
        if isOddPrimeGreaterThan100(number):
            if number < smallest:
                secondSmallest = smallest
                smallest = number
            elif number < secondSmallest:
                secondSmallest = number
    return secondSmallest