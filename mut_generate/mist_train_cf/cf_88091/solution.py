"""
QUESTION:
Write a function named `find_pairs` that takes a one-dimensional array of integers and a target integer as input. The function should find and print all pairs of numbers in the array that have a sum equal to the target value without using any additional data structures. The time complexity of the function should be O(n^2), where n is the total number of elements in the array.
"""

def find_pairs(array, target):
    n = len(array)
    if n < 2:
        return

    array.sort()
    left = 0
    right = n - 1

    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == target:
            print(array[left], array[right])
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1