"""
QUESTION:
Create a function named `count_odd_numbers` that takes a 2D array as input and returns the total count of odd numbers in the array, excluding any sub-array whose first element is odd.
"""

def entrance(arr):
    odd_count = 0
    for subarray in arr:
        if subarray[0] % 2 == 0: 
            for number in subarray:
                if number % 2 != 0: 
                    odd_count += 1
    return odd_count