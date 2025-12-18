"""
QUESTION:
An array is called *lovely* if the sum of product of each adjacent pair of elements is odd.

More formally, the array S of size M is lovely if the value \sum_{i=1}^{M-1} (S_{i} . S_{i+1}) is odd.

You are given an array A consisting of N positive integers. Find a [permutation] of array A which is *lovely*. 

If multiple such permutations are possible, output any. If there is no *lovely* permutation, output -1.

------ Input Format ------ 

- The first line contains an integer T denoting the number of test cases. The T test cases then follow.
- The first line of each test case contains an integer N.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \dots, A_{N}.

------ Output Format ------ 

For each test case, if a *lovely* permutation of A is possible, print a single line containing N integers denoting the elements of any *lovely* permutation of A. Otherwise, print -1.

------ Constraints ------ 

$1 ≤T ≤1000$
$2 ≤N ≤500$
$1 ≤A_{i} ≤10^{6}$

------ subtasks ------ 

Subtask 1 (100 points): Original constraints.

----- Sample Input 1 ------ 
2
5
1 2 3 4 10
3
7 11 145
----- Sample Output 1 ------ 
3 1 10 2 4
-1
----- explanation 1 ------ 
Test Case $1$: The sum of products of adjacent pair of elements of the given array is $1\cdot 2 + 2\cdot 3 + 3\cdot 4 + 4\cdot 10 = 2+6+12+40 = 60$. Since this value is even, this is not a *lovely* permutation of the array.  
A *lovely* permutation of the given array is $[3, 1, 10, 2, 4]$. The sum of products for this array would be $3\cdot 1 + 1\cdot 10 + 10\cdot 2 + 2\cdot 4 = 41$, which is odd.

Test Case $2$: No permutation of the given array exists where the sum of products of adjacent pair of elements is odd. Thus, answer is $-1$.
"""

def find_lovely_permutation(test_cases):
    results = []
    
    for case in test_cases:
        N, A = case
        p1, p2 = 0, 0
        
        for i in A:
            if i % 2 == 1:
                p1 += 1
            else:
                p2 += 1
        
        if p1 == 0 or (p2 == 0 and p1 % 2 == 1) or p1 == 1:
            results.append(-1)
        else:
            s1, s2 = [], []
            for i in A:
                if i % 2 == 1:
                    s1.append(i)
                else:
                    s2.append(i)
            
            if p1 % 2 == 1:
                s2.append(s1.pop())
            
            lovely_permutation = s1 + s2
            results.append(lovely_permutation)
    
    return results