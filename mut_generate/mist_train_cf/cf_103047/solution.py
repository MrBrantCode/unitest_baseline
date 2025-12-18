"""
QUESTION:
Write a function named `find_second_highest` that takes an array of numbers as input and returns the second highest element in the array. Do not use the built-in max() or sort() functions. The function should return None if there is no second highest element. The time complexity of the solution should be O(n), where n is the length of the array.
"""

def find_second_highest(arr):
    if len(arr) < 2:
        return None

    highest = float('-inf')
    second_highest = float('-inf')

    for num in arr:
        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num

    if second_highest == float('-inf'):
        return None
    else:
        return second_highest