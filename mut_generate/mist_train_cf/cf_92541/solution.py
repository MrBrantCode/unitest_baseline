"""
QUESTION:
Write a function named `column_sums` that takes a 2D array as input and returns a list containing the sums of all columns. The time complexity of the solution must be O(n), where n is the total number of elements in the array.
"""

def column_sums(array):
    column_sums = []
    for row in array:
        for i, num in enumerate(row):
            if len(column_sums) <= i:
                column_sums.append(num)
            else:
                column_sums[i] += num
    return column_sums