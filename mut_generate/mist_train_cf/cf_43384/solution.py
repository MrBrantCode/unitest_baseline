"""
QUESTION:
Write a function `find_fruit_position(food_matrix, fruit_name)` that takes a 2-dimensional matrix of unique fruit names and a specific fruit name, and returns the row and column index of the fruit in the matrix as a tuple. If the fruit does not exist in the matrix, return 'Fruit not found'.
"""

def find_fruit_position(food_matrix, fruit_name):
    for i, row in enumerate(food_matrix):
        if fruit_name in row:
            return (i, row.index(fruit_name))
    return 'Fruit not found'