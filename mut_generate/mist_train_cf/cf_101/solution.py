"""
QUESTION:
Create a function named `generate_array(N)` that generates an NxN array where each row and column sum up to N and have unique sums. The function should have a time complexity of less than O(N^2) and a space complexity of less than O(N^2).
"""

def generate_array(N):
    result = [[0] * N for _ in range(N)]

    for i in range(N):
        result[i][i] = 1

        for j in range(N):
            if j != i:
                result[i][j] = 1
                result[j][i] = 1

    return result