"""
QUESTION:
Find the two elements in an unsorted array of positive integers that have the largest sum. The array may contain duplicates and can have a maximum length of 10^6. If there are multiple pairs with the same maximum sum, return any one of them. Do not use any built-in sorting functions and ensure the solution has a time complexity of O(n) and a space complexity of O(1).
"""

def entrance(arr):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return [largest, second_largest]