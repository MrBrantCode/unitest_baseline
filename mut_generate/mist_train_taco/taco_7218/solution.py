"""
QUESTION:
Given an array of N integers and Q queries, each query having a range from index L to R. Find the maximum prefix-sum for the range L to R.
Note: Assume 0 based indexing.
Example 1:
Input: 
a[ ] = {-1, 2, 3, -5} 
Q = 2
L_{1} = 0, R_{1} = 3
L_{2} = 1, R_{2} = 3
Output:
4 5
Explanation:
The range (0, 3) in the 1st query is {-1, 2, 3, -5}, hence, 
the max prefix-sum will be -1 + 2 + 3 = 4. The range (1, 3) 
in the 2nd query is {2, 3, -5}, hence, the max prefix-sum 
will be 2 + 3 = 5.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxPrefixes() which takes the array A[], its size N, array L[] and R[] and their size Q as input parameters and returns a vector storing the required answer for every query.
Expected Time Complexity: O(N*Q)
Expected Auxiliary Space: O(1)
Constraints: 
1 ≤ N ≤ 10^{4}
-10^{4} ≤ A[i]≤ 10^{4}
1 ≤ Q ≤ 10^{4}
0 ≤ L[i] ≤ R[i] < N
"""

def max_prefix_sums(a, L, R, N, Q):
    # Compute the prefix sums
    for i in range(N - 1):
        a[i + 1] += a[i]
    a.insert(0, 0)
    
    # Initialize the output list
    output = []
    
    # Process each query
    for i in range(Q):
        # Calculate the maximum prefix-sum for the current query
        max_prefix_sum = max(a[L[i] + 1:R[i] + 2]) - a[L[i]]
        output.append(max_prefix_sum)
    
    return output