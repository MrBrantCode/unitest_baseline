"""
QUESTION:
Create a function named `get_adjacent_numbers` that takes a 2D array as input. The function should return a list of adjacent numbers (horizontal, vertical, and diagonal) of each number in the array. The function should not return any number more than once and should not consider any number outside the boundaries of the array.
"""

def get_adjacent_numbers(arr):
    rows = len(arr)
    cols = len(arr[0])
    adjacent_numbers = set()
    
    for i in range(rows):
        for j in range(cols):
            # Horizontal adjacent numbers
            if j + 1 < cols:
                adjacent_numbers.add(arr[i][j + 1])
            if j - 1 >= 0:
                adjacent_numbers.add(arr[i][j - 1])
            
            # Vertical adjacent numbers
            if i + 1 < rows:
                adjacent_numbers.add(arr[i + 1][j])
            if i - 1 >= 0:
                adjacent_numbers.add(arr[i - 1][j])
            
            # Diagonal adjacent numbers
            if i - 1 >= 0 and j - 1 >= 0:
                adjacent_numbers.add(arr[i - 1][j - 1])
            if i - 1 >= 0 and j + 1 < cols:
                adjacent_numbers.add(arr[i - 1][j + 1])
            if i + 1 < rows and j - 1 >= 0:
                adjacent_numbers.add(arr[i + 1][j - 1])
            if i + 1 < rows and j + 1 < cols:
                adjacent_numbers.add(arr[i + 1][j + 1])
    
    return list(adjacent_numbers)