"""
QUESTION:
Create a function named `retrieve_last_three_unique_elements` that takes an array of integers as input and returns a new array containing the last three unique elements from the input array, sorted in ascending order. The function should iterate through the input array from the end and stop once it has found three unique elements. If the input array has less than three unique elements, return all unique elements in the array, also in ascending order.
"""

def retrieve_last_three_unique_elements(arr):
    if len(arr) < 3:
        return arr
    unique_elements = []
    for i in range(len(arr)-1, -1, -1):
        if arr[i] not in unique_elements:
            unique_elements.append(arr[i])
            if len(unique_elements) == 3:
                break
    return sorted(unique_elements)