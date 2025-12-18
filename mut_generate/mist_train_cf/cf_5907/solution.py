"""
QUESTION:
Write a function named `zigzagSum` that calculates the sum of elements in a given 2D array accessed in a zigzag pattern. The function should take a 2D array as input and return the sum of the elements accessed in the zigzag pattern. The time complexity of the solution should be O(n), where n is the total number of elements in the array.
"""

def zigzagSum(arr):
    row = 0
    col = 0
    sum_elements = 0
    num_rows = len(arr)
    num_cols = len(arr[0])

    for _ in range(num_rows * num_cols):
        sum_elements += arr[row][col]
        
        if row % 2 == 0:
            if col == num_cols - 1:
                row += 1
            else:
                col += 1
        else:
            if col == 0:
                row += 1
            else:
                col -= 1
                
    return sum_elements