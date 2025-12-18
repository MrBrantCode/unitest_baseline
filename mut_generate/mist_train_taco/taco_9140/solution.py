"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 
Sereja has an array A that contains n integers: A_{1}, A_{2}, ..., A_{n}. 
Sereja also has an array B that contains n integers B_{1}, B_{2}, ..., B_{n}. 
In a single step Sereja can choose two indexes i and j (1 ≤ i ≤ j ≤ n) , and increase all the elements of A with indices between i and j inclusively by one, modulo 4.
In other words, we make A_{p} equal to (A_{p} + 1) modulo 4 if p is an integer from the range [i; j].

Now Sereja is interested in the following question: what is the mininal number of steps necessary in order to make the array A equal to the array B.

------ Input ------ 

The first line contains an integer T - the number of the testcases. Then, T tests follow. 

The first line of each testcase contains the integer n. 

The next line conatins n single space separated integers - A_{1}, A_{2}, ..., A_{n}. 

The next line conatin n single space separated integers - B_{1}, B_{2}, ..., B_{n}.

------ Output ------ 

For each testcase output an answer - the mininal number of steps necessary.

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ n ≤ 10^{5}$
$0 ≤ A_{i}, B_{i} ≤ 3$

------ Example ------ 

Input:
1
5
2 1 3 0 3
2 2 0 1 0

Output:
1
"""

def min_steps_to_transform_array(A, B):
    n = len(A)
    for i in range(n):
        B[i] = (B[i] + 4 - A[i]) % 4
    
    i = n - 1
    while i > 0:
        B[i] -= B[i - 1]
        i -= 1
    
    ans = 0
    s2 = 0
    s3 = 0
    for i in range(n):
        if B[i] < 2:
            ans += max(B[i], 0)
            if B[i] == -2:
                s2 += 1
            if B[i] == -3:
                s3 += 1
        else:
            if s3 > 0:
                s3 -= 1
                ans += 1
                B[i] -= 4
            elif s2 > 0:
                s2 -= 1
                ans += 2
                B[i] -= 4
            ans += max(B[i], 0)
            if B[i] == -2:
                s2 += 1
            if B[i] == -3:
                s3 += 1
    
    return ans