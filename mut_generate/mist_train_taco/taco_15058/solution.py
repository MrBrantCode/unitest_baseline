"""
QUESTION:
Read problem statements in [Mandarin], [Bengali], and [Russian] as well.

You are handed a binary string S, but not in any ordinary form. Instead of being directly given the value of S, you are given an array C of size N representing the *01-compression representation* of S. This means S first contains C_{1} \texttt{0} characters, then C_{2} \texttt{1} characters, then C_{3} \texttt{0} characters, and so on. For example, the array C = [2, 3, 4, 3] corresponds with the binary string \texttt{001110000111}.

You are allowed to modify S by swapping elements of C. More specifically, you are allowed to swap C_{i} and C_{j} *as long as* C_{i} and C_{j} both encodes blocks of the same character. For example, from C = [2, 3, 4, 3], you can swap C_{1} and C_{3} because both of them encode blocks of \texttt{0}'s, turning C to [4, 3, 2, 3] and S to \texttt{000011100111}. However, you cannot swap C_{1} and C_{2} because C_{1} encodes a block of \texttt{0}'s, while C_{2} encodes a block of \texttt{1}s.

Perform the swapping operation in any way as many times as you want (including zero times) so that the final string S has as many \texttt{01} subsequences as possible. As a reminder, a subsequence of a string is a sequence that can be derived by deleting zero or more characters without changing the order of the remaining characters.

You need to find any optimal final array C, for which the number of \texttt{01} subsequence will be the largest possible.

------ Input Format ------ 

- The first line contains T - the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer N - the size of the array C.
- The second line of each test case contains N integers C_{1}, C_{2}, \dots, C_{N} - the \texttt{01}-compression representation of S.

------ Output Format ------ 

For each test case, output two lines: the first line contains N integers representing the optimal array C, and the second line contains the maximum number of \texttt{01} subsequences.

------ Constraints ------ 

$ 1 ≤ T ≤ 1000 $
$ 1 ≤ N ≤ 100 $
$ 1 ≤  C_{i} ≤ 1000 $

----- Sample Input 1 ------ 
1
4
2 3 4 3
----- Sample Output 1 ------ 
4 3 2 3
30
----- explanation 1 ------ 
- Test case $1$: $C = [2, 3, 4, 3]$, which means $S$ corresponds to $\texttt{001110000111}$. The optimal list of operations is to only swap $C_{1}$ and $C_{3}$, resulting in $C = [4, 3, 2, 3]$ and $S = $ $\texttt{000011100111}$, which has $30$ subsequences of $\texttt{01}$.
"""

def maximize_01_subsequences(C, N):
    ones = []
    zeros = []
    i = 0
    while i < N:
        if i % 2 == 0:
            zeros.append(C[i])
        else:
            ones.append(C[i])
        i += 1
    
    ones.sort()
    zeros.sort(reverse=True)
    
    optimal_C = []
    i = 0
    j = 0
    k = 0
    while len(optimal_C) != N:
        if k % 2 == 0:
            optimal_C.append(zeros[i])
            i += 1
        else:
            optimal_C.append(ones[j])
            j += 1
        k += 1
    
    ones_sum = 0
    i = 0
    while i < N:
        if i % 2 == 1:
            ones_sum += optimal_C[i]
        i += 1
    
    max_01_subsequences = 0
    i = 0
    while i < N:
        if i % 2 == 0:
            max_01_subsequences += optimal_C[i] * ones_sum
        else:
            ones_sum = max(0, ones_sum - optimal_C[i])
        i += 1
    
    return optimal_C, max_01_subsequences