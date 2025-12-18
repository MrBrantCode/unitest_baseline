"""
QUESTION:
Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
 
Example 1:
Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.
Example 2:
Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.
Your Task:
The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{7}
0 ≤ A_{i} ≤ 10^{6}
"""

def find_majority_element(A, N):
    if N == 1:
        return A[0]
    
    majority_count = N // 2
    element_count = {}
    
    for element in A:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    for element, count in element_count.items():
        if count > majority_count:
            return element
    
    return -1