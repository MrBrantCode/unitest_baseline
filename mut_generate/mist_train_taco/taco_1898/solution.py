"""
QUESTION:
You are given an array A of length N. 

The *interesting value* of a subarray is defined as the product of the maximum and minimum elements of the subarray.

Find the minimum and maximum *interesting value* over all subarrays for the given array.

Note: A subarray is obtained by deletion of several (possibly zero) elements from the beginning of the array and several (possibly zero) elements from the end of the array.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The first line of each test case contains an integer N - the length of the array A.
- The second line of each test case contains N space-separated integers A_{1},A_{2},\ldots,A_{N}.

------ Output Format ------ 

For each test case, output two space-separated integers on a new line the minimum and maximum *interesting value* over all subarrays for the given array.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 10^{5}$
$-10^{9} ≤ A_{i} ≤ 10^{9}$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^{5}$.

----- Sample Input 1 ------ 
2
2
2 2
3
5 0 9

----- Sample Output 1 ------ 
4 4
0 81
----- explanation 1 ------ 
Test case $1$: The minimum *interesting value* possible is $4$. A subarray with *interesting value* equal to $4$ is $[2,2]$. Here, both minimum and maximum elements of the subarray are $2$. It can be proven that no subarray of the array has *interesting value* less than $4$.  
The maximum *interesting value* possible is $4$. A subarray with *interesting value* equal to $4$ is $[2,2]$. Here, both minimum and maximum elements of the subarray are $2$. It can be proven that no subarray of the array has *interesting value* greater than $4$.

Test case $2$: The minimum *interesting value* possible is $0$. A subarray with *interesting value* equal to $0$ is $[5, 0, 9]$. Here, minimum element is $0$ and maximum element is $9$. It can be proven that no subarray of the array has *interesting value* less than $0$.  
The maximum *interesting value* possible is $81$. A subarray with *interesting value* equal to $81$ is $[9]$. Here, both minimum and maximum elements of the subarray are $9$. It can be proven that no subarray of the array has *interesting value* more than $81$.
"""

def find_min_max_interesting_values(A, N):
    if N == 0:
        return (0, 0)  # Edge case: empty array
    
    # Initialize variables to store the minimum and maximum values
    min_val = A[0]
    max_val = A[0]
    min_abs_val = abs(A[0])
    max_abs_val = abs(A[0])
    
    # Iterate through the array to find the required values
    for i in range(1, N):
        if A[i] < min_val:
            min_val = A[i]
        if A[i] > max_val:
            max_val = A[i]
        min_abs_val = min(min_abs_val, abs(A[i]))
        max_abs_val = max(max_abs_val, abs(A[i]))
    
    # Calculate the minimum and maximum interesting values
    min_interesting_value = min(min_val * max_val, min_abs_val * min_abs_val)
    max_interesting_value = max_abs_val * max_abs_val
    
    return (min_interesting_value, max_interesting_value)