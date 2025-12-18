"""
QUESTION:
Write a function `find_max_element` that takes a 2D array of integers as input and returns the maximum element in the array. The array can contain both positive and negative integers. The function should have a time complexity of O(n*m), where n is the number of rows and m is the number of columns, and a space complexity of O(1).
"""

def find_max_element(arr):
    max_element = float('-inf')  

    for row in arr:
        for num in row:
            if num > max_element:
                max_element = num

    return max_element