"""
QUESTION:
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.


Note that it is the kth smallest element in the sorted order, not the kth distinct element.


Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.



Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
"""

def find_kth_smallest_in_matrix(matrix, k):
    arr = []
    for row in matrix:
        for element in row:
            arr.append(element)
    arr.sort()
    return arr[k - 1]