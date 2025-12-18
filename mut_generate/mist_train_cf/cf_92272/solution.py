"""
QUESTION:
Design a function `countAndSumEvenNumbers` that takes an array of integers as input, counts the total number of even numbers, and calculates the sum of all even numbers in the array. The function should be efficient enough to handle arrays with up to 10^6 elements.
"""

def countAndSumEvenNumbers(arr):
    count = 0
    sum = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
            sum += num
    return count, sum