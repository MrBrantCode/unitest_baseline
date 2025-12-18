"""
QUESTION:
Create a function named 'generate_array' that generates an NxN array with all elements equal to 1, ensuring that each row and column sum up to N. The function should have a time complexity of less than O(N^2) and take an integer 'N' as its input.
"""

def generate_array(N):
    arr = [[0] * N for _ in range(N)]
    row_sums = [N] * N
    col_sums = [N] * N

    for i in range(N):
        for j in range(N):
            if row_sums[i] > 0 and col_sums[j] > 0:
                arr[i][j] = 1
                row_sums[i] -= 1
                col_sums[j] -= 1

    return arr