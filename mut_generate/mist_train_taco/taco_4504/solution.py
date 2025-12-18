"""
QUESTION:
An array A of length N is said to be *pseudo-sorted* if it can be made non-decreasing after performing the following operation at most once.
Choose an i such that 1 ≤ i ≤ N-1 and swap A_{i} and A_{i+1}

Given an array A, determine if it is *pseudo-sorted* or not.

------ Input Format ------ 

- The first line contains a single integer T - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer N - the size of the array A.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \dots, A_{N} denoting the array A.

------ Output Format ------ 

For each testcase, output YES if the array A is pseudo-sorted, NO otherwise.

You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$2 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases do not exceed $2 \cdot 10^{5}$

----- Sample Input 1 ------ 
3
5
3 5 7 8 9
4
1 3 2 3
3
3 2 1

----- Sample Output 1 ------ 
YES
YES
NO

----- explanation 1 ------ 
Test case 1: The array is already sorted in non-decreasing order.

Test case 2: We can choose $i = 2$ and swap $A_{2}$ and $A_{3}$. The resulting array will be $[1, 2, 3, 3]$, which is sorted in non-decreasing order.

Test case 3: It can be proven that the array cannot be sorted in non-decreasing order in at most one operation.
"""

def is_pseudo_sorted(A):
    """
    Determines if the array A is pseudo-sorted.

    An array A is pseudo-sorted if it can be made non-decreasing after performing
    the following operation at most once:
    Choose an i such that 1 ≤ i ≤ N-1 and swap A[i] and A[i+1].

    Parameters:
    A (list of int): The array to be checked.

    Returns:
    str: "YES" if the array is pseudo-sorted, "NO" otherwise.
    """
    N = len(A)
    sorted_A = sorted(A)
    moves = 0
    
    for i in range(N):
        if A[i] != sorted_A[i]:
            if i == N - 1:
                return "NO"
            else:
                A[i], A[i + 1] = A[i + 1], A[i]
                moves += 1
                if moves > 1:
                    return "NO"
    
    return "YES"