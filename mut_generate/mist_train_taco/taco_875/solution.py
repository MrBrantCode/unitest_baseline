"""
QUESTION:
Given an array A[ ] of N integers and an integer X. In one operation, you can change the i^{th} element of the array to any integer value where 1 ≤ i ≤ N. Calculate minimum number of such operations required such that the bitwise AND of all the elements of the array is strictly greater than X.
Example 1:
Input:
N = 4, X = 2
A[] = {3, 1, 2, 7}
Output: 
2
Explanation: 
After performing two operations:
Modified array: {3, 3, 11, 7} 
Now, Bitwise AND of all the elements
is 3 & 3 & 11 & 7 = 3 
Example 2:
Input:
N = 3, X = 1
A[] = {2, 2, 2}
Output: 
0
Your Task:
You don't need to read input or print anything. Your task is to complete the function count( ) which takes N, A[ ] and X as input parameters and returns the minimum number of operations required.
Expected Time Complexity: O(N * Log(max(A[ ])))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{9}
1 ≤ X ≤ 10^{9}
"""

def minimum_operations_to_bitwise_and_greater_than_x(N, A, X):
    res = N
    bitset = 0
    
    for i in range(32, -1, -1):
        if X & (1 << i) > 0:
            bitset |= 1 << i
        else:
            count = 0
            temp = bitset | (1 << i)
            for num in A:
                if (num & temp) != temp:
                    count += 1
            res = min(res, count)
    
    return res