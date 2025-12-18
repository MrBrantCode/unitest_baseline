"""
QUESTION:
An array is called *interesting* if no subarray of length greater than 2 is non-increasing or non-decreasing.

Chef has an array A of length N. He wants to make the array interesting by rearranging the elements in any order. 

If there exist multiple such arrays, output any one.  
If no such array exists, print -1 instead.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
- The first line of each test case contains an integer N denoting the length of array A.
- The next line contains N space separated integers, A_{1}, A_{2}, \ldots, A_{N}

------ Output Format ------ 

For each test case, output on a single line, any possible interesting array.
If no such array is possible, output -1.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^{5}$.

----- Sample Input 1 ------ 
3
3
2 2 2
4
2 6 5 2
5
5 5 2 4 2
----- Sample Output 1 ------ 
-1
6 2 5 2
5 2 4 2 5

----- explanation 1 ------ 
Test case $1$: There is no way of arranging the elements such that no subarray of length greater than $2$ is non-increasing or non-decreasing.

Test case $2$: A possible rearrangement of the elements is $[6, 2, 5, 2]$. Note that the subarrays of length greater than $2$ are $\{[6, 2, 5], [2, 5, 2], [6, 2, 5, 2]\}$. None of these subarrays are non-increasing or non-decreasing.

Test case $3$: A possible rearrangement of the elements is $[5, 2, 4, 2, 5]$. Note that the subarrays of length greater than $2$ are $\{[5, 2, 4], [2, 4, 2], [4, 2, 5], [5, 2, 4, 2], [2, 4, 2, 5], [5, 2, 4, 2, 5]\}$. None of these subarrays are non-increasing or non-decreasing.
"""

def make_interesting_array(A, N):
    if N < 3:
        return A  # Any array of length less than 3 is trivially interesting
    
    A.sort()
    greater = A[N // 2:]
    lesser = A[:N // 2]
    valid = []
    
    for i in range(N // 2):
        valid.append(greater[i])
        valid.append(lesser[i])
    
    if N % 2 == 1:
        valid.append(greater[-1])
    
    interest = True
    for i in range(1, N - 1):
        if not (valid[i - 1] < valid[i] > valid[i + 1] or valid[i - 1] > valid[i] < valid[i + 1]):
            interest = False
            break
    
    if interest:
        return valid
    else:
        return -1