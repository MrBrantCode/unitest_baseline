"""
QUESTION:
Given two arrays A[] and B[] consisting of N and M elements respectively. The task is to find minimum number of elements to remove from each array such that no common element exist in both the arrays.
 
Example 1:
Input :
A[] = { 2, 3, 4, 5, 8 }
B[] = { 1, 2, 3, 4}
Output :
3
Explanation:
We need to remove 2, 3 and 4 from any 
array.
 
Example 2:
Input :
A[] = { 4, 2, 4, 4}
B[] = { 4, 3 }
Output :
1
Explanation:
We need to remove 4 from B[]
 
Example 3:
Input:
A[] = { 1, 2, 3, 4 }
B[] = { 5, 6, 7 }
Output:
0
Explanation:
There is no common element in both.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minRemove() which takes the array A[], B[] and its size N, M as inputs and returns the minimum number of elements to be deleted.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1<=N,M<=10^{5}
1<=A[i],B[i]<=10^{5}
"""

from collections import Counter

def min_remove(A, B):
    # Convert arrays to sets to find common elements
    s1 = set(A)
    s2 = set(B)
    
    # Find the intersection of both sets
    common_elements = s1.intersection(s2)
    
    # Initialize the answer to 0
    ans = 0
    
    # Count the frequency of elements in both arrays
    c1 = Counter(A)
    c2 = Counter(B)
    
    # For each common element, add the minimum count from both arrays to the answer
    for v in common_elements:
        ans += min(c1[v], c2[v])
    
    # Return the total number of elements to remove
    return ans