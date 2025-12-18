"""
QUESTION:
Write a function `invert_array` that inverts the order of a multidimensional array without using any predefined or built-in methods. The function should reverse both the outermost array and each nested array. The function should be able to handle arrays of varying lengths and depths. The solution should have optimal time and space complexity.
"""

def invert_array(arr):
    # Base case, if array is empty then return an empty array
    if not arr:
        return []
      
    if type(arr[0]) is list:
        # If the head of array is a list, recursively invert this array
        return invert_array(arr[1:]) + [invert_array(arr[0])]
    else:
        # If the head of array is not a list, recursively invert the rest of array and add head to the end
        return invert_array(arr[1:]) + [arr[0]]