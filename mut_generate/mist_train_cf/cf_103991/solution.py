"""
QUESTION:
Write a function `find_two_largest(numbers)` that takes an array of integers as input and returns an array containing the two largest numbers in the input array. The output should be in descending order. If there are fewer than two numbers in the array, return an empty array. If there are multiple occurrences of the largest number, consider only one occurrence in the result.
"""

def find_two_largest(numbers):
    if len(numbers) < 2:
        return []
    
    max1 = float('-inf')
    max2 = float('-inf')
    
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2 and num < max1:
            max2 = num
    
    return [max1, max2]