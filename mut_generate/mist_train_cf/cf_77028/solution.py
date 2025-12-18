"""
QUESTION:
Write a function `kthSmallest(matrix, k)` that returns the kth smallest element in an n x n matrix after removing duplicates, where each row and column is sorted in ascending order. The function must take two parameters: a 2D list `matrix` and an integer `k`, and return the kth smallest element. The input matrix is guaranteed to be square (n == matrix.length == matrix[i].length), 1 <= n <= 300, and -10^9 <= matrix[i][j] <= 10^9. The value of k is guaranteed to be 1 <= k <= n^2.
"""

import heapq

def kthSmallest(matrix, k):
    min_heap = []
    n = len(matrix)
    for r in range(min(k, n)): 
        min_heap.append((matrix[r][0], r, 0))  

    heapq.heapify(min_heap)

    number, r, c = 0, 0, -1
    while k > 0 and min_heap:
        number, r, c = heapq.heappop(min_heap)

        if len(min_heap) == 0 or min_heap[0][0] != number or k == 1:  
            k -= 1

        if c < n - 1:  
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

    return number