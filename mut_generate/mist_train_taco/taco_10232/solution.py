"""
QUESTION:
Concatenation of two integers is obtained as follows: First, convert both integers to strings. Then concatenate both strings into one and convert this concatenated string back to integer.

For example, concatenation of 6 and 7 is CONC(6, 7) = 67, concatenation of 123 and 45 is CONC(123, 45) = 12345.

You are given an array A consisting of N integers. You are also given two integers L and R. Find the number of pairs (i, j) such that  1 ≤ i, j ≤ N and   L ≤ CONC(A_{i}, A_{j}) ≤ R

Note: Since the size of the input and output is large, please use fast input-output methods.

------ Input Format ------ 

- The first line will contain T, the number of test cases. Then T test cases follow.
- The first line of each test case contains three integers N, L, R.
- The second line of each test case line contains N integers A_{1}, A_{2},\dots, A_{N}. 

------ Output Format ------ 

For each testcase, output in a single line the number of suitable pairs.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ L ≤ R ≤ 10^{15}$
$1 ≤ A_{i} ≤ 10^{7}$
- Sum of $N$ over all test cases does not exceed $10^{6}$.

----- Sample Input 1 ------ 
4
2 10 52
2 5
3 58 100
4 2 3
4 100 1000
1 10 100 1000
5 28 102
3 2 1 9 10

----- Sample Output 1 ------ 
3
0
2
11

----- explanation 1 ------ 
Test case 1: 

- $(i = 1, j = 1)$: $CONC(A_{1}, A_{1}) = 22$ and $10 ≤ 22 ≤ 52$.

- $(i = 1, j = 2)$: $CONC(A_{1}, A_{2}) = 25$ and $10 ≤ 25 ≤ 52$.

- $(i = 2, j = 1)$: $CONC(A_{2}, A_{1}) = 52$ and $10 ≤ 52 ≤ 52$.

- $(i = 2, j = 2)$: $CONC(A_{2}, A_{2}) = 55$ and $10 ≤ 55$ but $ 55 \nleq 52$.

So there are three suitable pairs.

Test case 2: There is no suitable pair.

Test case 3: The suitable pairs are $(2, 1)$ and $(1, 2)$.
"""

def count_suitable_pairs(N, L, R, A):
    l1 = []
    r1 = []
    l2 = 0
    r2 = N - 1
    
    # Calculate l1 array
    for j in range(N - 1, -1, -1):
        while l2 < N and (not L <= int(str(A[l2]) + str(A[j]))):
            l2 += 1
        l1.append(l2)
    
    # Calculate r1 array
    for k in range(N):
        while r2 >= 0 and (not int(str(A[r2]) + str(A[k])) <= R):
            r2 -= 1
        r1.append(r2)
    
    l1.reverse()
    s = 0
    
    # Calculate the number of suitable pairs
    for z in range(N):
        x = r1[z] - l1[z] + 1
        if x > 0:
            s += x
    
    return s