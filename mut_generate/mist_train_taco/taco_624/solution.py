"""
QUESTION:
Given a binary matrix  having n rows and m columns, your task is to find the sum of coverage of all zeros in the matrix where coverage for a particular 0 is defined as total number of ones around a zero in left, right, up and bottom directions.
 
Example 1:
Input: matrix = {{0, 1, 0},
{0, 1, 1}, {0, 0, 0}}
Output: 6
Example 2:
Input: matrix = {{0, 1}}
Output: 1
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function FindCoverage() which takes the matrix as input parameter and returns sum of coverage of all zeros in the matrix.
 
Expected Time Complexity: O(n * m)
Expected Space Complexity: O(1)
 
Constraints:
1 <= n, m <= 100
"""

def calculate_zero_coverage(matrix):
    coverage_total = 0
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if j - 1 >= 0 and matrix[i][j - 1] == 1:
                    coverage_total += 1
                if j + 1 < m and matrix[i][j + 1] == 1:
                    coverage_total += 1
                if i - 1 >= 0 and matrix[i - 1][j] == 1:
                    coverage_total += 1
                if i + 1 < n and matrix[i + 1][j] == 1:
                    coverage_total += 1
    
    return coverage_total