"""
QUESTION:
Given an array A[]of size N. Let us call difference between indices of an element's first and last appearance in the array A[] a gap. Find the maximum possible gap.  Note that if any element appears only once, then the gap for that element is 0.
 
Example 1:
Input:
N = 9
A[] = {2, 1, 3, 4, 2, 1, 5, 1, 7}
Output:
6
Explanation:
For the above test case (Assuming 0-based indexing): 
Number 1's first appearance is at index 1 and last appearance is at index 7. This implies gap is 7-1=6
This is the maximum possible in the given test case.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function leftIndex() which takes the array A[] and its size N as inputs and returns the Maximum Difference.
 
Expected Time Complexity: O(N. Log(N))
Expected Auxiliary Space: O(N)
 
Constraints:
1<=N<=10^{5}
-10^{5}<=A_{i}<=10^{5}
"""

def find_maximum_gap(A, N):
    maxi = -math.inf
    dicti = {}
    for i in range(N):
        if A[i] not in dicti:
            dicti[A[i]] = i
        else:
            maxi = max(maxi, i - dicti[A[i]])
    if maxi == -math.inf:
        return 0
    return maxi