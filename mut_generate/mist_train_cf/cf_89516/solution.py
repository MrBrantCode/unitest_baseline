"""
QUESTION:
Convert the given matrix into a list of lists where the duplicate elements in each row are removed and the resulting list of lists is sorted in descending order based on the sum of the elements in each row. The given matrix contains n rows and m columns where n and m are positive integers, the elements in each row are in ascending order, and the elements in each column are in descending order. Implement the function `convert_matrix(matrix)` with a time complexity of O(n+m).
"""

def entrance(matrix):
    result = []
    row_dict = {}

    for row in matrix:
        current_row = []
        for element in sorted(row, reverse=True):
            if element not in row_dict:
                current_row.append(element)
                row_dict[element] = 1
            else:
                row_dict[element] += 1
        result.append(current_row)

    result.sort(key=sum, reverse=True)

    return result