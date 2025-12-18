"""
QUESTION:
Create a function `most_common_element` that takes an array of elements as input and returns the most common element in the array. The function should have a time complexity of O(nlogn), where n is the size of the array.
"""

def most_common_element(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Initialize variables to store the current element being counted and its count
    current_element = arr[0]
    current_count = 1
    
    # Initialize variables to store the most common element and its count
    most_common_element = arr[0]
    most_common_count = 1
    
    # Iterate through the sorted array
    for i in range(1, len(arr)):
        if arr[i] == current_element:
            current_count += 1
        else:
            if current_count > most_common_count:
                most_common_element = current_element
                most_common_count = current_count
            current_element = arr[i]
            current_count = 1
    
    # Check the last element's count
    if current_count > most_common_count:
        most_common_element = current_element
        most_common_count = current_count
    
    return most_common_element