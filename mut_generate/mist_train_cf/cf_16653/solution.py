"""
QUESTION:
Create a function named `append_elements` that takes two parameters: an array and a number of elements to append at the end. The function should return the updated array if the array is not empty, the number of elements to append is less than or equal to half the length of the array, and the sum of the elements in the array after appending is divisible by 3. Otherwise, return an error message indicating the reason for the failure. The time complexity of the function should be O(n), where n is the length of the array.
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