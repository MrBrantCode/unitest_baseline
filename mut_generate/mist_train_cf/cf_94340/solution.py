"""
QUESTION:
Create a function called `append_elements` that takes in a list of elements `array` and a number of elements `num_elements` to append at the end of the array. The function should return the updated array or an error message based on the following conditions:

- If the array is empty, return "Array is empty".
- If the number of elements to append is more than half the length of the array, return "Number of elements to append is too large".
- If the sum of the elements in the array after appending is divisible by 3, return the updated array. Otherwise, return "Sum of elements in the array after appending is not divisible by 3".

The function should have a time complexity of O(n), where n is the length of the array.
"""

def append_elements(array, num_elements):
    if len(array) == 0:
        return "Array is empty"
    
    if num_elements > len(array) // 2:
        return "Number of elements to append is too large"
    
    array += [0] * num_elements
    
    if sum(array) % 3 == 0:
        return array
    else:
        return "Sum of elements in the array after appending is not divisible by 3"