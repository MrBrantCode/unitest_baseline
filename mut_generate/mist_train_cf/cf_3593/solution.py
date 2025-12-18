"""
QUESTION:
Create a function called `sum_of_each_row` that takes a 2D array of numbers as input and returns a list of integers representing the sum of each row. Each row should be sorted in ascending order and duplicate elements should be ignored before calculating the sum. The sum of each row should be rounded to the nearest whole number. The function should have a time complexity of O(n^2) and a space complexity of O(n), where n is the total number of elements in the array. The function should handle negative numbers, large numbers, and decimal numbers.
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