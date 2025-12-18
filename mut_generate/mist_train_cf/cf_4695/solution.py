"""
QUESTION:
Implement a function `find_smallest` that takes an array of integers `arr` as input and returns the smallest number in the array. The function should have a time complexity of O(n), where n is the size of the array, and use constant space complexity. The implementation should use a single loop and not rely on built-in functions such as `min()`, sorting, or any other optimization techniques that result in a time complexity less than O(n).
"""

def find_smallest(arr):
    smallest = arr[0]  # Initialize smallest as the first element of the array

    for num in arr:
        if num < smallest:
            smallest = num  # Update smallest if the current number is smaller

    return smallest