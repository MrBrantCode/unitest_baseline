"""
QUESTION:
Write a function named find_min_info that calculates the minimum value in a 2D list of lists, its corresponding position(s) (row, column), and its frequency in the array without using built-in Python functions like min(). The function should return the minimum value, a list of its positions, and its frequency. Assume that the input 2D list is not empty and all sublists have the same length.
"""

def find_min_info(arr):
    min_value = arr[0][0]
    min_positions = [(0, 0)]
    count = 1
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < min_value:
                min_value = arr[i][j]
                min_positions = [(i, j)]
                count = 1
            elif arr[i][j] == min_value:
                min_positions.append((i, j))
                count += 1

    return min_value, min_positions, count