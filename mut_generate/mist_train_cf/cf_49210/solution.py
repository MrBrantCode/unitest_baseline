"""
QUESTION:
Write a function called `sums` that takes a two-dimensional array as input. The function should return the total sum of all elements, the sum of elements in each row, the sum of elements in each column, the sum of elements in the main diagonal, and a list of sums that are either equal to the total sum or appear more than once in the row, column, or diagonal sums.
"""

def sums(data):
    total_sum = sum(sum(row) for row in data)
    row_sums = [sum(row) for row in data]
    column_sums = [sum(data[i][j] for i in range(len(data))) for j in range(len(data[0]))]
    diagonal_sum = sum(data[i][i] for i in range(len(data)))

    matching_sums = []
    all_sums = row_sums + column_sums + [diagonal_sum]
    
    for s in all_sums:
        if s == total_sum or all_sums.count(s) > 1:
            matching_sums.append(s)

    return total_sum, row_sums, column_sums, diagonal_sum, list(set(matching_sums))