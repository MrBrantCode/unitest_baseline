"""
QUESTION:
Given an array A of size N. The contents of A are copied into another array B and numbers are shuffled. Also, one element is removed from B. The task is to find the missing element.
 
Example 1:
Input : 
A[] = {4, 8, 1, 3, 7}
B[] = {7, 4, 3, 1}
Output : 8
Explanation:
8 is the only element missing from B.
 
Example 2:
Input : 
A[] = {12, 10, 15, 23, 11, 30}
B[] = {15, 12, 23, 11, 30}
Output : 10
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findMissing() which takes the array A[], B[] and its size N and N-1, respectively as inputs and returns the missing number.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
2 <= N <= 10^{6}
1 <= A, B <= 10^{18}
Array may also contain duplicates.
"""

def find_missing(A, B):
    return sum(A) - sum(B)