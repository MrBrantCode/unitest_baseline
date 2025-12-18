"""
QUESTION:
Write a function called `third_largest` that takes an array of integers as input and returns the third largest unique number in the array. If the array has less than three unique numbers, the function should return `None`. The function should be able to handle negative numbers.
"""

def third_largest(arr):
    # Remove duplicates by turning the array into a set
    unique_arr = list(set(arr))

    # If there are less than 3 unique numbers, return None
    if len(unique_arr) < 3:
        return None
    else:
        # Sort the array in descending order
        unique_arr.sort(reverse=True)

        # Return the third largest number
        return unique_arr[2]