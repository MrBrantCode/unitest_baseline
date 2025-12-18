"""
QUESTION:
Design a function `countAndSumEvenNumbers` that takes an array of integers as input and returns a tuple containing two values: the total count of even numbers and the sum of all even numbers in the array. The function should be able to handle arrays with up to 10^6 elements.
"""

def countAndSumEvenNumbers(arr):
    count = 0
    total_sum = 0
    for num in arr:
        if num % 2 == 0:
            count += 1
            total_sum += num
    return count, total_sum