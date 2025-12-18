"""
QUESTION:
You are given two arrays A and B, each of size N. You can perform the following types of operations on array A.

Type 1: Select any prefix of A and increment all its elements by 1.
Type 2: Select any suffix of A and increment all its elements by 1.

Your task is to transform the array A into array B using the minimum number of operations. If it is impossible to do so, output -1.

For an array A having N elements:
A prefix of the array A is a subarray starting at index 1.
A suffix of the array A is a subarray ending at index N.

------ Input Format ------ 

- First line will contain T, number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer N, the size of arrays A and B.
- The next line contains N space-separated integers, where the i^{th} integer denotes A_{i}.
- The next line contains N space-separated integers, where the i^{th} integer denotes B_{i}.

------ Output Format ------ 

For each test case, print a single line containing one integer ―  minimum operations required to convert A into B. Print -1 if it is impossible to convert A into B.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$1 ≤ N ≤ 10^{5}$
$ -10^{14} ≤ A_{i}, B_{i} ≤ 10^{14} $
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
3
5
2 3 5 1 2
4 3 6 2 3
4
0 0 0 0
1 2 2 1
3
1 2 3
1 2 2
----- Sample Output 1 ------ 
3
2
-1
----- explanation 1 ------ 
Test Case $1$: Given $A = [2,3,5,1,2]$. It can be converted to array $B = [4, 3, 6, 2, 3]$ in $3$ operations:
- Operation $1$: Perform a type $1$ operation. Choose the prefix of length $1$ and increment the elements by $1$. Thus, the updated array is $A = [3, 3, 5, 1, 2]$.
-  Operation $2$: Perform a type $1$ operation. Choose the prefix of length $1$ and increment the elements by $1$. Thus, the updated array is $A = [4, 3, 5, 1, 2]$.
- Operation $3$: Perform a type $2$ operation. Choose the suffix of length $3$ and increment the elements by $1$. Thus, the updated array is $A = [4, 3, 6, 2, 3]$.

It can be proven that we cannot convert the array $A$ into array $B$ in less than $3$ operations.

Test Case $2$: Given $A = [0,0,0,0]$. It can be converted to array $B = [1,2,2,1]$ in $2$ operations:
- Operation $1$: Perform a type $1$ operation. Choose the prefix of length $3$ and increment the elements by $1$. Thus, the updated array is $A = [1,1,1,0]$.
-  Operation $2$: Perform a type $2$ operation. Choose the suffix of length $3$ and increment the elements by $1$. Thus, the updated array is $A = [1,2,2,1]$.

It can be proven that we cannot convert the array $A$ into array $B$ in less than $2$ operations.

Test Case $3$: Given $A = [1,2,3]$. The value of $A[3]$ will always be greater than $B[3]$. Hence, it is impossible to convert $A$ into $B$ using any number of operations.
"""

def min_operations_to_transform(A, B):
    """
    Calculate the minimum number of operations required to transform array A into array B.
    
    Parameters:
    A (list of int): The initial array.
    B (list of int): The target array.
    
    Returns:
    int: The minimum number of operations required, or -1 if it is impossible.
    """
    n = len(A)
    if n != len(B):
        return -1
    
    op1, op2 = B[0] - A[0], 0
    res1, res2 = 0, 0
    
    for i in range(n):
        if op1 + op2 < B[i] - A[i]:
            op2 += B[i] - A[i] - op1 - op2
        elif op1 + op2 > B[i] - A[i]:
            op1 -= op1 + op2 - (B[i] - A[i])
        
        if op1 < 0 or op2 > B[n - 1] - A[n - 1]:
            return -1
        
        res1 = max(res1, op1)
        res2 = max(res2, op2)
    
    return res1 + res2