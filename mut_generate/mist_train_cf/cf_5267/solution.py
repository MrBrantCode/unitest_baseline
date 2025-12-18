"""
QUESTION:
Write a function `findSecondLargest` that takes an array of numbers as input and returns the second largest number in the array. The function should have a time complexity of O(n), where n is the length of the array. If there is no second largest number (i.e., all numbers in the array are the same), the function should return the smallest possible value (e.g., negative infinity).
"""

def findSecondLargest(numbers):
    largest = float('-inf')
    secondLargest = float('-inf')
    
    for num in numbers:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
            secondLargest = num
            
    return secondLargest