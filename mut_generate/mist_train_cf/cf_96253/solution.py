"""
QUESTION:
Write a function `find_max_element` that takes a 2D array of size n x m as input, where n is the number of rows and m is the number of columns. The array can contain both positive and negative integers. The function should return the maximum element in the array with a time complexity of O(n*m) and a space complexity of O(1).
"""

def find_max_element(arr):
    max_element = float('-inf')
    for row in arr:
        for num in row:
            if num > max_element:
                max_element = num
    return max_element