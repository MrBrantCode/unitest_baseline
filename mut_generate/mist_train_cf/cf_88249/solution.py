"""
QUESTION:
Create a function `generate_matrices(N)` that generates N 4x4 matrices, each containing random integers between -100 and 100, and returns the sum of the diagonal elements of each matrix. 

Constraints: 
- N is a positive integer less than or equal to 10^6.
- The function should have a time complexity of O(N).
- The function should have a space complexity of O(N).
- Do not use built-in functions or libraries for generating random numbers.
"""

def entrance(N):
    diagonal_sums = []
    for _ in range(N):
        matrix = [[(i * 110 + j) % 200 - 100 for j in range(4)] for i in range(4)]
        diagonal_sum = sum(matrix[i][i] for i in range(4))
        diagonal_sums.append(diagonal_sum)
    return diagonal_sums