"""
QUESTION:
Write a function named `removeGreaterThanTen` that takes an array of integers as input and returns a new array containing only the elements that are less than or equal to 10.
"""

def removeGreaterThanTen(arr): 
    # Create a new_arr array
    new_arr = [] 

    # Iterate each element in array
    for i in range(len(arr)):

        # Check if the element is greater than 10
        if arr[i] <= 10: 
            # Add the element to the new_arr
            new_arr.append(arr[i]) 

    return new_arr