"""
QUESTION:
There is an integer sequence of length 2^N: A_0, A_1, ..., A_{2^N-1}. (Note that the sequence is 0-indexed.)
For every integer K satisfying 1 \leq K \leq 2^N-1, solve the following problem:
 - Let i and j be integers. Find the maximum value of A_i + A_j where 0 \leq i < j \leq 2^N-1 and (i or j) \leq K.
Here, or denotes the bitwise OR.

-----Constraints-----
 - 1 \leq N \leq 18
 - 1 \leq A_i \leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N
A_0 A_1 ... A_{2^N-1}

-----Output-----
Print 2^N-1 lines.
In the i-th line, print the answer of the problem above for K=i.

-----Sample Input-----
2
1 2 3 1

-----Sample Output-----
3
4
5

For K=1, the only possible pair of i and j is (i,j)=(0,1), so the answer is A_0+A_1=1+2=3.
For K=2, the possible pairs of i and j are (i,j)=(0,1),(0,2).
When (i,j)=(0,2), A_i+A_j=1+3=4. This is the maximum value, so the answer is 4.
For K=3, the possible pairs of i and j are (i,j)=(0,1),(0,2),(0,3),(1,2),(1,3),(2,3) .
When (i,j)=(1,2), A_i+A_j=2+3=5. This is the maximum value, so the answer is 5.
"""

def find_max_sum_pairs(N: int, A: list) -> list:
    A.append(float('-inf'))  # Append a very small value to handle edge cases
    dp = []
    ans = 0
    aaa = []
    
    for i in range(2 ** N):
        if i == 0:
            dp.append((0, -1))
            continue
        
        (na, nb) = (i, -1)
        for j in range(N):
            if 2 ** j & i > 0:
                (ta, tb) = dp[i ^ 2 ** j]
                if A[na] < A[ta]:
                    nb = na
                    na = ta
                elif A[nb] < A[ta] and ta != na:
                    nb = ta
                if A[nb] < A[tb]:
                    nb = tb
        
        ans = max(A[na] + A[nb], ans)
        aaa.append(ans)
        dp.append((na, nb))
    
    return aaa