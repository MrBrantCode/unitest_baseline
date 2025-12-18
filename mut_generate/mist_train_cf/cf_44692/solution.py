"""
QUESTION:
Create a function `third_largest` that takes an array of numbers as input and returns the third largest number in the array. The array must contain at least three elements. If the array has fewer than three elements, the function should return an error message. The function should be able to handle arrays with duplicate elements, in which case it should return the third largest unique number.
"""

def third_largest(arr):
    # Check if array is less than 3
    if len(arr) < 3:
        return "Array should have at least 3 elements!"

    # Remove duplicates from the array
    unique_arr = list(set(arr))
    
    # Check if array is less than 3 after removing duplicates
    if len(unique_arr) < 3:
        return "Array should have at least 3 unique elements!"

    # Sort the array in descending order
    sorted_arr = sorted(unique_arr, reverse=True)
    
    # Get the third largest number from sorted array
    third_largest_num = sorted_arr[2]

    return third_largest_num