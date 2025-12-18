"""
QUESTION:
Implement a function `find_submatrix_indices(array1, array2)` that finds the indices of the first occurrence of a submatrix in `array1` that matches `array2`. The time complexity should be less than O(n^4), where n is the size of `array1`, and the space complexity should be less than O(n^2). If no matching submatrix is found, return `None`.
"""

def find_submatrix_indices(array1, array2):
    n1, m1 = len(array1), len(array1[0])
    n2, m2 = len(array2), len(array2[0])

    for i in range(n1 - n2 + 1):
        for j in range(m1 - m2 + 1):
            match = True
            for row in range(n2):
                for col in range(m2):
                    if array1[i+row][j+col] != array2[row][col]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return (i, j)

    return None