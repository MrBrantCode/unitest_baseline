"""
QUESTION:
Write a function find_submatrix_indices(array1, array2) that finds the indices of the first occurrence of a submatrix in array1 that matches array2. The function should return a tuple (i, j) representing the top-left indices of the submatrix, or None if no match is found. The time complexity should be less than O(n^4), where n is the size of the larger matrix.
"""

def find_submatrix_indices(array1, array2):
    n1, m1 = len(array1), len(array1[0])
    n2, m2 = len(array2), len(array2[0])
    
    for i in range(n1 - n2 + 1):
        for j in range(m1 - m2 + 1):
            match = True
            for k in range(n2):
                for l in range(m2):
                    if array1[i + k][j + l] != array2[k][l]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return (i, j)
    
    return None