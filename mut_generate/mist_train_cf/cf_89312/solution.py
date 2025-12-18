"""
QUESTION:
Write a recursive function `count_occurrences(arr, x)` that takes an array `arr` and an integer `x` as arguments and returns the number of times `x` appears in `arr`. The function should have a time complexity of O(n), where n is the number of elements in `arr`, and should not use any built-in methods or libraries. The function should iterate through the array only once.
"""

def entance(arr, x):
    # Check if the array is empty
    if len(arr) == 0:
        return 0

    count = 0

    # Check if the first element is equal to x
    if arr[0] == x:
        count += 1

    # Create a new array without the first element
    new_arr = arr[1:]

    # Call the recursive function again with the new array and x
    count += entance(new_arr, x)

    # Add the return value of the recursive function to the count variable
    return count