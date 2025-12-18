"""
QUESTION:
Given a matrix of size n x n such that it has only one 0, Find the positive number (greater than zero) to be placed in place of the 0 such that sum of the numbers in every row, column and two diagonals become equal. If no such number exists, return -1.
Note: Diagonals should be only of the form matrix[i][i] and matrix[i][n-i-1]. n is always greater than 1. The answer can be greater than 10^{9}. 
 
Example 1:
Input: matrix = {{5, 5}, {5, 0}}
Output: 5
Explanation: The matrix is
5 5
5 0
Therefore If we place 5 instead of 0, all
the element of matrix will become 5. 
Therefore row 5+5=10, column 5+5=10 and 
diagonal 5+5=10, all are equal.
Example 2:
Input: matrix = {{1, 2, 0}, {3, 1, 2}, 
{2, 3, 1}}
Output: -1
Explanation: It is not possible to insert 
an element in place of 0 so that the 
condition is satisfied.thus result is -1. 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function MissingNo() which takes the matrix as input parameter and returns the number which should be placed in place of 0 such that the condition gets satisfied. If not possible return -1.
 
Expected Time Complexity: O(n * n)
Expected Space Complexity: O(2 * n)
 
Constraints:
2 <= n <= 1000
1 <= elements in the matrix <= 10^9
"""

def find_missing_number(matrix):
    n = len(matrix)
    total_sum = 0
    zero_row_sum = 0
    zero_row_index = -1
    
    # Find the sum of a row without 0 and the row with 0
    for i in range(n):
        row_sum = sum(matrix[i])
        if 0 in matrix[i]:
            zero_row_sum = row_sum
            zero_row_index = i
        else:
            total_sum = row_sum
            break
    
    # Calculate the number to replace 0
    if total_sum == 0:
        return -1
    
    missing_number = total_sum - zero_row_sum
    
    # Replace 0 with the missing number
    zero_col_index = matrix[zero_row_index].index(0)
    matrix[zero_row_index][zero_col_index] = missing_number
    
    # Check if all rows, columns, and diagonals have the same sum
    expected_sum = total_sum
    sums = []
    
    # Check row sums
    for i in range(n):
        sums.append(sum(matrix[i]))
    
    # Check column sums
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        sums.append(col_sum)
    
    # Check diagonal sums
    diag1_sum = 0
    diag2_sum = 0
    for i in range(n):
        diag1_sum += matrix[i][i]
        diag2_sum += matrix[i][n - i - 1]
    sums.append(diag1_sum)
    sums.append(diag2_sum)
    
    # If all sums are equal and the missing number is positive, return it
    if len(set(sums)) == 1 and missing_number > 0:
        return missing_number
    
    return -1