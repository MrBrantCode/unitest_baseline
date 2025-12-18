"""
QUESTION:
Given an array A consisting of N distinct integers (1 ≤ A_{i} ≤ 2 \cdot N), we have to perform K moves.
We perform the following steps in one move:

Select an integer X such that 1 ≤ X ≤ 2 \cdot N and X \ne A_{i} for all i (X is not equal to any element of the current array).
Append X to A.
The *score* of this move = (\max_{1 ≤ i ≤ |A|} A_{i}) - X.  
Note that the *score* is calculated after appending X. Thus, X can be the maximum element of the array as well.

For e.g. if A = [3, 1, 5] and we append X = 2 to A, then, A becomes [3, 1, 5, 2] and the *score* of this move is \max([3, 1, 5, 2]) - 2 = 5 - 2 = 3.

Find the maximum sum of *scores* we can achieve after performing exactly K moves.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains three space-separated integers N and K — the size of the array A and the number of moves respectively.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \dots, A_{N} denoting the array A.

------ Output Format ------ 

For each test case, output the maximum sum of *scores* we can achieve after performing exactly K moves.  
It is guaranteed that it is always possible to perform K moves under the given constraints. 

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$1 ≤K ≤N$
$1 ≤ A_{i} ≤ 2 \cdot N$
- All $A_{i}$ are distinct.
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
3 1
1 3 6
2 2
1 2
3 2
1 2 5

----- Sample Output 1 ------ 
4
1
3

----- explanation 1 ------ 
Test Case 1: We can perform the following move:
- Append $X = 2$. Score of this move $= \max([1, 3, 6, 2]) - 2 = 6 - 2 = 4$

Hence, the maximum total score is $4$.

Test Case 2: We can perform the following moves:
- Append $X = 4$. Score of this move $= \max([1, 2, 4]) - 4 = 4 - 4 = 0$
- Append $X = 3$. Score of this move $= \max([1, 2, 4, 3]) - 3 = 4 - 3 = 1$

Hence, the maximum total score is $0+1=1$.

Test Case 3: We can perform the following moves:
- Append $X = 4$. Score of this move $= \max([1, 2, 5, 4]) - 4 = 5 - 4 = 1$
- Append $X = 3$. Score of this move $= \max([1, 2, 5, 4, 3]) - 3 = 5 - 3 = 2$

Hence the maximum total score is $1+2=3$.
"""

def calculate_max_score(N, K, A):
    B = []
    m = max(A)
    M = 2 * N
    count = 0
    
    # Check if 1 is not in A, then add it
    if min(A) != 1:
        count = 1
        B.append(1)
        A.append(1)
        N += 1
    
    sum1 = 0
    sum2 = 0
    A.sort()
    
    # Fill B with the missing numbers between the elements of A
    for j in range(N - 1):
        d = A[j + 1] - A[j]
        if A[j + 1] - A[j] > 1:
            for l in range(d - 1):
                B.append(A[j] + 1 + l)
                count += 1
                if count == K:
                    break
        if count == K:
            break
    
    # If count is still less than K, fill the rest with numbers greater than max(A)
    if count < K:
        for j in range(K - count):
            B.append(m + 1 + j)
    
    # Calculate the scores
    for j in range(K):
        sum1 += m - B[j]
        sum2 += M - B[j]
    
    sum2 -= M - B[K - 1]
    
    return max(sum1, sum2)