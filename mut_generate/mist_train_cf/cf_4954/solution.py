"""
QUESTION:
Create a function named `divisible_by_3_greater_than_2_with_7` that takes an array of integers as input and returns a new array containing only the elements that are divisible by 3, greater than 2, and contain the digit 7. The function should have a time complexity of O(n) and a space complexity of O(m), where n is the length of the input array and m is the number of elements that meet the criteria.
"""

def divisible_by_3_greater_than_2_with_7(arr):
    result = []
    for num in arr:
        if num % 3 == 0 and num > 2 and '7' in str(num):
            result.append(num)
    return result