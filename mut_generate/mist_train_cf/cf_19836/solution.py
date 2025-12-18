"""
QUESTION:
Create a function called `copy_array` that takes an input array and returns a new array consisting of all odd numbers smaller than 5 from the input array. The length of the new array should not exceed 5. If no such numbers exist, return an empty array. The function should be implemented in a recursive manner.
"""

def copy_array(arr):
    """
    Creates a new array consisting of all odd numbers smaller than 5 from the input array.
    The length of the new array should not exceed 5. If no such numbers exist, return an empty array.
    
    Args:
        arr (list): The input array.
    
    Returns:
        list: A new array consisting of odd numbers smaller than 5 from the input array.
    """
    # Base case: if the input array is empty, return an empty array
    if len(arr) == 0:
        return []
    
    # Recursive case: check if the first element is smaller than 5 and odd
    if arr[0] < 5 and arr[0] % 2 != 0:
        # Create a new array by concatenating the first element with the result of the recursive call on the rest of the array
        result = [arr[0]] + copy_array(arr[1:])
        # Limit the length of the new array to 5
        return result[:5]
    else:
        # Return the result of the recursive call on the rest of the array
        return copy_array(arr[1:])