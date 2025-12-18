"""
QUESTION:
Write a function named `find_max_element` to find the maximum element in a 2D array of size n x m, where n is the number of rows and m is the number of columns. The function should be able to handle arrays containing both positive and negative integers. The time complexity should be O(n*m) and the space complexity should be O(1).
"""

def find_max_element(arr):
    max_element = float('-inf')  

    for row in arr:
        for num in row:
            if num > max_element:
                max_element = num

    return max_element