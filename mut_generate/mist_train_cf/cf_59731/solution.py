"""
QUESTION:
Implement a function named `compress_matrix` that compresses a multidimensional matrix of integers using the Run-Length Encoding (RLE) algorithm. The function should take a 2D list of integers as input and return a compressed 2D list where identical "runs" of values are replaced with the value and its count. For example, the row `[2, 2, 2, 5, 5, 5, 5, 1, 1]` becomes `[[2, 3], [5, 4], [1, 2]]`. The function should handle edge cases such as empty matrices or matrices with a large number of zeros. Provide a complexity analysis of the algorithm in terms of time and space.
"""

def compress_matrix(matrix):
    if not matrix or not matrix[0]: 
        return []

    compressed_matrix = []

    for row in matrix: 
        compressed_row = []
        current = row[0]
        count = 1

        for element in row[1:]:
            if element == current:
                count += 1
            else:
                compressed_row.append([current, count])
                current = element
                count = 1

        compressed_row.append([current, count])  
        compressed_matrix.append(compressed_row)

    return compressed_matrix