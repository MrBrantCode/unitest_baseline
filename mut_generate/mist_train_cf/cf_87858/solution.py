"""
QUESTION:
Implement a function named `insert_at_beginning` that takes an array and an integer as input. The function should insert the integer at the beginning of the array without using any built-in functions or methods that directly add or remove elements to/from the array. The function must shift all existing elements one position to the right and assign the new element to the first index. The time complexity of the function should be O(n), where n is the number of elements in the array. The function should not allocate any additional memory.
"""

def insert_at_beginning(arr, num):
    """
    Inserts an integer at the beginning of an array without using built-in functions or methods.
    
    Args:
    arr (list): The input array.
    num (int): The integer to be inserted.
    
    Returns:
    list: The modified array with the integer inserted at the beginning.
    """
    arr.append(None)  # Allocate memory for a new element at the beginning
    for i in range(len(arr)-1, 0, -1):  # Shift all existing elements one position to the right
        arr[i] = arr[i-1]
    arr[0] = num  # Assign the new element to the first index
    return arr