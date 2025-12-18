"""
QUESTION:
Write a function named `find_pairs` that takes a one-dimensional array of integers and a target integer as input. The function should find and print all pairs of numbers in the array that have a sum equal to the target value, with a time complexity of O(n^2), where n is the total number of elements in the array. The function should not use any additional data structures to store the pairs.
"""

def find_pairs(array, target):
    n = len(array)
    if n < 2:
        return

    # Sort the array in non-decreasing order
    array.sort()

    # Initialize two pointers, one at the beginning and one at the end of the array
    left = 0
    right = n - 1

    # Traverse the array from both ends towards the middle
    while left < right:
        current_sum = array[left] + array[right]

        # If the current sum equals the target, print the pair and move both pointers
        if current_sum == target:
            print(array[left], array[right])
            left += 1
            right -= 1
        # If the current sum is less than the target, move the left pointer to the right
        elif current_sum < target:
            left += 1
        # If the current sum is greater than the target, move the right pointer to the left
        else:
            right -= 1