"""
QUESTION:
Implement a function `insert_element(array, element)` that adds an element to a sorted array while maintaining the array's sorted order. The function should have a time complexity of O(n), where n is the length of the array, and a space complexity of O(1), without using any built-in sorting functions or libraries.
"""

def insert_element(array, element):
    # If the array is empty, simply append the element
    if not array:
        array.append(element)
        return array

    # Find the index where the element should be inserted
    index = 0
    while index < len(array) and array[index] < element:
        index += 1

    # Shift all elements to the right from the insert index
    array.append(None)
    for i in range(len(array) - 1, index, -1):
        array[i] = array[i - 1]

    # Insert the element at the appropriate index
    array[index] = element

    return array