"""
QUESTION:
Construct a function `min_pair_diff(arr)` that determines the minimal difference between any two elements within a given array and returns the pair of elements with this minimal difference. The function should accept an array that may contain both integers and floating-point numbers, and it should disregard non-numeric elements. If the array is empty or contains less than two numeric elements, the function should return a message indicating that at least two elements are needed or at least two numeric elements are needed, respectively.
"""

def min_pair_diff(arr):
    # Edge case: No elements
    if len(arr) == 0:
        return "At least 2 elements are needed"
    # If only 1 numeric element.
    if len(list(filter(lambda x: isinstance(x, (int, float)), arr))) == 1:
        return "At least 2 numeric elements are needed"
    num_arr = [x for x in arr if isinstance(x, (int, float))]
    num_arr.sort()
    diff = float('inf')
    for i in range(len(num_arr)-1):
        if num_arr[i+1] - num_arr[i] < diff:
            diff = num_arr[i+1] - num_arr[i]
            pair = (num_arr[i], num_arr[i+1])
    return pair