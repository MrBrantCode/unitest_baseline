"""
QUESTION:
Write a function named `insert_element` that inserts a new element into an existing unsorted array at a specified index without using any built-in array functions or methods. The array is unsorted and the insertion point is determined by the first element in the array that is greater than or equal to the new element. The function should return the modified array. The function should achieve a time complexity of O(n), where n is the size of the original array.
"""

def insert_element(arr, element):
    size = len(arr)
    new_arr = [None] * (size + 1)
    insert_index = 0
    
    # Find the index to insert the new element
    while insert_index < size and arr[insert_index] < element:
        insert_index += 1
    
    # Copy elements before the insertion point
    for i in range(insert_index):
        new_arr[i] = arr[i]
    
    # Insert the new element
    new_arr[insert_index] = element
    
    # Copy remaining elements
    for i in range(insert_index + 1, size + 1):
        new_arr[i] = arr[i - 1]
    
    # Update the original array reference
    arr = new_arr
    
    return arr