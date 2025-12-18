"""
QUESTION:
Read problems statements in mandarin chinese, russian and vietnamese as well. 

Given a board of N rows and M columns, place the minimum number of knights such that every cell either contains a knight or is attacked by at least one knight.

Like in standard chess, a knight attacks every cell that is two squares away horizontally and one square vertically, or two squares vertically and one square horizontally.

------ Input ------ 

The first line of input contains one number T, the number of test cases.
Each test case contains two integers N and M, the dimensions of the board.

------ Output ------ 

For each test case print the minimum number of knights required to cover every cell of the board.

------ Constraints ------ 

1 ≤ T ≤ 150
1 ≤ N ≤ 3
1 ≤ M ≤ 50

----- Sample Input 1 ------ 
1
2 4
----- Sample Output 1 ------ 
4
----- explanation 1 ------ 
One optimal configuration is:

Cells (1, 1), (1, 2), (4, 1) and (4, 2) contain knights. Cell (2, 1) is attacked by the knight in cell (4, 2). Cell (2, 2) is attacked by the knight in cell (4, 1). Cell (3, 1) is attacked by the knight in cell (1, 2). And cell (3, 2) is attacked by the knight in cell (1, 1).
So every cell either contains a knight or is attacked by at least one knight, hence this is a valid configuration. There is no valid configuration with fewer knights, and so the answer is 4.
"""

def minimum_knights_required(N, M):
    # Ensure N is the smaller dimension and M is the larger dimension
    if M < N:
        N, M = M, N
    
    if N == 1:
        return M
    else:
        res = M // 6 * 4
        if M % 6 > 0:
            if M % 6 == 1:
                res += 2
            elif N == 3 and M > 12 and (M % 6 == 2):
                res += 3
            else:
                res += 4
        return res