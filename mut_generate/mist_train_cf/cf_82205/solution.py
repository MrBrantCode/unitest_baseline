"""
QUESTION:
Create a function named `reverse_array` that constructs a novel array consisting of elements in the reverse order from the original one. The function should not use any built-in reverse methods and should have a linear time complexity. The original array must remain unmodified.
"""

def reverse_array(arr):
    new_arr = [0]*len(arr) # Create a new array of the same size
    for i in range(len(arr)):
        new_arr[i] = arr[len(arr)-1-i] # Assign elements in reverse order
    return new_arr