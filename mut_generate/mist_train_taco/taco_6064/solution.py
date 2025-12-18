"""
QUESTION:
You are given a N * N matrix, U. You have to choose 2 sub-matrices A and B made of only 1s of U, such that, they have at least 1 cell in common, and each matrix is not completely engulfed by the other, i.e., 

If U is of the form 

and A is of the form

and B is of the form

then, there exists atleast 1 a_{i, j} : a_{i, j} ∈ A and a_{i,j} ∈ B 

then, there exists atleast 1 ai1, j1 : ai1, j1 ∈ A and ai1,j1 ∉ B 

then, there exists atleast 1 ai2, j2 : ai2, j2 ∈ B and ai2,j2 ∉ A 

a_{x,y} = 1 ∀ a_{x,y} ∈ A 

a_{x,y} = 1 ∀ a_{x,y} ∈ B  

How many such (A, B) exist?

Input Format 

The first line of the input contains a number N. 

N lines follow, each line containing N integers (0/1) NOT separated by any space.

Output Format 

Output the total number of such (A, B) pairs. If the answer is greater than or equal to 10^{9} + 7,
then print answer modulo (%) 10^{9} + 7.

Constraints  

2 ≤ N ≤ 1500 

a_{i,j} ∈ [0, 1] : 0 ≤ i, j ≤ N - 1

Sample Input

4
0010
0001
1010
1110

Sample Output

10

Explanation

X means the common part of A and B. 

We can swap A and B to get another answer. 

0010
0001
A010
XB10

0010
0001
A010
XBB0

0010
0001
10A0
1BX0

0010
0001
10A0
BBX0

0010
0001
1010
AXB0

TimeLimits

Time limit for this challenge is mentioned here
"""

def count_valid_submatrices(matrix, n):
    MOD = 10 ** 9 + 7
    
    def check_valid(matrix, ARS, ACS, ARE, ACE):
        for i in range(ARS, ARE + 1):
            for j in range(ACS, ACE + 1):
                if matrix[i][j] != 1:
                    return False
        return True
    
    def check_common(ARS, ACS, ARE, ACE, BRS, BCS, BRE, BCE):
        if ARS <= BRE and ARE >= BRS and ACS <= BCE and ACE >= BCS:
            return True
        return False
    
    def check_not_engulfed(ARS, ACS, ARE, ACE, BRS, BCS, BRE, BCE):
        if ARS >= BRS and ACS >= BCS and ARE <= BRE and ACE <= BCE:
            return False
        if BRS >= ARS and BCS >= ACS and BRE <= ARE and BCE <= ACE:
            return False
        return True
    
    dp = []
    count = 0
    
    for ARS in range(n):
        for ACS in range(n):
            if matrix[ARS][ACS] == 0:
                continue
            for ARE in range(ARS, n):
                for ACE in range(ACS, n):
                    valid_a = check_valid(matrix, ARS, ACS, ARE, ACE)
                    if not valid_a:
                        continue
                    dp.append([ARS, ACS, ARE, ACE])
    
    for x in range(len(dp)):
        for y in range(x + 1, len(dp)):
            matrixA = dp[x]
            matrixB = dp[y]
            common = check_common(matrixA[0], matrixA[1], matrixA[2], matrixA[3], matrixB[0], matrixB[1], matrixB[2], matrixB[3])
            if not common:
                continue
            not_engulfed = check_not_engulfed(matrixA[0], matrixA[1], matrixA[2], matrixA[3], matrixB[0], matrixB[1], matrixB[2], matrixB[3])
            if not_engulfed:
                count = (count + 1) % MOD
    
    return count * 2