"""
QUESTION:
Generate an NxN array with all its elements equal to 1, ensuring that each row and column sum up to N. Each row and column should have a unique sum. The function name should be `generate_array(N)` and it should take an integer `N` as input. The time complexity should be less than O(N^2) and the space complexity should be less than O(N^2).
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