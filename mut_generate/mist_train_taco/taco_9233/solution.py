"""
QUESTION:
Given an array of positive integers and many queries for divisibility. In every query Q[i], we are given an integer K , we need to count all elements in the array which are perfectly divisible by K.
 
Example 1:
Input:
N = 6
A[] = { 2, 4, 9, 15, 21, 20}
M =  3
Q[] = { 2, 3, 5}
Output:
3 3 2
Explanation:
Multiples of '2' in array are:- {2, 4, 20}
Multiples of '3' in array are:- {9, 15, 21}
Multiples of '5' in array are:- {15, 20}
 
Example 2:
Input:
N = 3
A[] = {3, 4, 6}
M = 2
Q[] = {2, 3}
Output:
2 2
Your Task:  
You don't need to read input or print anything. Your task is to complete the function leftElement() which takes the array A[] and its size N, array Q[] and its size M as inputs and returns the array containing the required count for each query Q[i].
 
Expected Time Complexity: O(Mx*log(Mx))
Expected Auxiliary Space: O(Mx)
where Mx is the maximum value in array elements.
 
Constraints:
1<=N,M<=10^{5}
1<=A[i],Q[i]<=10^{5}
"""

from collections import Counter

def count_divisibles(A, Q):
    # Create a Counter object for the array A
    s = Counter(A)
    # Find the maximum value in the array A
    m = max(A)
    # Initialize the result list with zeros
    ans = [0] * len(Q)
    
    # Iterate over each query in Q
    for i, e in enumerate(Q):
        # If the query is not zero, count the multiples of e in A
        if e != 0:
            for k in range(e, m + 1, e):
                ans[i] += s.get(k, 0)
    
    return ans