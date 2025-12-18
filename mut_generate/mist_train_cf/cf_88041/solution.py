"""
QUESTION:
Create a function `sum_of_each_row` that takes a 2D array as input and returns a list of integers, where each integer is the sum of a row in the input array. The function should meet the following requirements:

- Time complexity: O(n^2), where n is the total number of elements in the array.
- Space complexity: O(n), where additional data structures are proportional to the input size.
- Each row should be sorted in ascending order before calculating the sum.
- Duplicate elements in a row should be ignored.
- The function should handle negative numbers, large numbers, and decimal numbers.
- Each sum should be rounded to the nearest whole number.
"""

def sum_of_each_row(array):
    def calculate_sum(row):
        sorted_row = sorted(set(row))
        row_sum = 0
        for element in sorted_row:
            row_sum += element
        return round(row_sum)

    result = []
    for row in array:
        result.append(calculate_sum(row))
    return result