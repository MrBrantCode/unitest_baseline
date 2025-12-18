"""
QUESTION:
Create a function sum_of_each_row that calculates the sum of each row in a given 2D array. The function should have a time complexity of O(n), where n is the total number of elements in the array, and a space complexity of O(1), excluding the space needed for the output. The function should be able to handle negative numbers and large numbers (greater than 32-bit integers).
"""

def sum_of_each_row(arr):
    row_sums = []
    for row in arr:
        row_sum = 0
        for num in row:
            row_sum += num
        row_sums.append(row_sum)
    return row_sums