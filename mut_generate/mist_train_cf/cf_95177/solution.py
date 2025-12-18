"""
QUESTION:
Create a function `sum_of_rows` that calculates the sum of each row in a given 2D array, with the following constraints: 
- Time complexity of O(n^2), where n is the total number of elements in the array.
- Space complexity of O(n), using additional data structures of size proportional to the input.
- The function should be able to handle negative numbers, large numbers (greater than 32-bit integers), and decimal numbers.
"""

def sum_of_rows(arr):
    row_sums = []  # to store the sum of each row
    for row in arr:
        current_sum = 0  # initialize the sum for the current row
        for element in row:
            current_sum += element  # add each element to the sum
        row_sums.append(current_sum)  # add the sum of the current row to the row_sums list
    return row_sums