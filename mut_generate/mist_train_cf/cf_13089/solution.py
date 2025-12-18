"""
QUESTION:
Write a function named `findMaxElement` to find the maximum element in a 2D array of size n x m. The function should have a time complexity of O(n*m) and a space complexity of O(1), where n is the number of rows and m is the number of columns in the array. The array contains only positive integers.
"""

def findMaxElement(arr):
    max_element = float('-inf')
    for row in arr:
        for element in row:
            if element > max_element:
                max_element = element
    return max_element