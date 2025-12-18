"""
QUESTION:
Given a sorted array A[] having 10 elements which contain 6 different numbers in which only 1 number is repeated five times. Your task is to find the duplicate number using two comparisons only.
Example 1:
Input: 
A[] = {1, 1, 1, 1, 1, 5, 7, 10, 20, 30}
Output: 1
Example 2:
Input: 
A[] = {1, 2, 3, 3, 3, 3, 3, 5, 9, 10}
Output: 3
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findDuplicate() which takes the array A[], as inputs and returns the required duplicate element.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
Size of the array A[] = 10
1 ≤ A[] ≤ 10^{5}
"""

def find_duplicate(A):
    # Since the array is sorted and has exactly 10 elements,
    # the duplicate number will be either at the 4th or 5th position.
    if A[4] == A[5]:
        return A[4]
    else:
        return A[5]