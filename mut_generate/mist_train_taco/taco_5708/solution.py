"""
QUESTION:
Given a matrix mat[][] of size N x M. The task is to find the largest rectangular sub-matrix by area whose sum is 0.
If there are multiple solutions return the rectangle which starts from minimum column index. If you still have multiple solutions return the one starting from minimum row index. If you still have multiple solutions return the one having greatest row number. If no such matrix is present return a zero (0) size matrix.
Example 1:
Input: N = 3, M = 3
mat[][] =  1, 2, 3
          -3,-2,-1
           1, 7, 5
Output:  1, 2, 3
        -3,-2,-1
Explanation: This is the largest sub-matrix,
whose sum is 0.
Example 2:
Input: N = 4, M = 4
mat[][] = 9, 7, 16, 5
          1,-6,-7, 3
          1, 8, 7, 9
          7, -2, 0, 10
 Output: -6,-7
          8, 7
         -2, 0 
Your Task:
You don't need to read input or print anything. You just have to complete the function sumZeroMatrix() which takes a 2D matrix mat[][], its dimensions N and M as inputs and returns a largest sub-matrix, whose sum is 0.
Expected Time Complexity: O(N*N*M).
Expected Auxiliary Space: O(N*M).
Constraints:
1 <= N, M <= 100
-1000 <= mat[][] <= 1000
"""

from typing import List

def find_largest_zero_sum_submatrix(mat: List[List[int]], N: int, M: int) -> List[List[int]]:
    (cLeft, cRight, rUp, rDown) = (0, M, 0, -N)

    def compare(tp1, tp2):
        A1 = (tp1[1] - tp1[0] + 1) * (tp1[3] - tp1[2])
        A2 = (tp2[1] - tp2[0] + 1) * (tp2[3] - tp2[2])
        if A1 > A2:
            return tp1
        elif A1 < A2:
            return tp2
        elif tp1[0] < tp2[0]:
            return tp1
        elif tp1[0] > tp2[0]:
            return tp2
        elif tp1[2] < tp2[2]:
            return tp1
        else:
            return tp2

    for cStart in range(M):
        temp = [0 for _ in range(N)]
        for cEnd in range(cStart, M):
            for i in range(N):
                temp[i] += mat[i][cEnd]
            countDict = {0: 0}
            currSum = 0
            for i in range(N):
                currSum += temp[i]
                if currSum in countDict:
                    (cLeft, cRight, rUp, rDown) = compare((cLeft, cRight, rUp, rDown), (cStart, cEnd, countDict[currSum], i + 1))
                else:
                    countDict[currSum] = i + 1

    if rDown == -N:
        return []
    else:
        return [row[cLeft:cRight + 1] for row in mat[rUp:rDown]]