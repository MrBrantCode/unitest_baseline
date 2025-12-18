"""
QUESTION:
Write a function called `sortArray` that takes an array of non-negative integers as input and returns a new array with the same elements but arranged differently. The arrangement depends on the sum of the first and last index values of the input array. If the sum is odd, the output array should be sorted in increasing order. If the sum is even, the output array should be sorted in decreasing order. If the sum is a prime number, intersperse values in increasing and decreasing order. The original array should not be modified.
"""

def sortArray(array):
    def checkPrime(num):
        for i in range(2, num):
            if num % i == 0: 
                return False
        return num > 1

    newArray = array[:] 

    if len(newArray) <= 1: 
        return newArray

    sum_val = newArray[0] + newArray[-1]

    if checkPrime(sum_val):
        sortedArray = sorted(newArray)
        resultArray = []
        for i in range(len(sortedArray)//2):
            resultArray.append(sortedArray[i])
            if sortedArray[-1-i]:
                resultArray.append(sortedArray[-1-i])
        return resultArray
    else:
        return sorted(newArray, reverse=(sum_val % 2 == 0))