"""
QUESTION:
Given an array A of N integers, find any 3 elements in it such that A[i] < A[j] < A[k] and i < j < k. 
Example 1:
Input:
N = 5
A[] = {1,2,1,1,3}
Output: 1
Explanation: a sub-sequence 1 2 3 exist.
Example 2:
Input:
N = 3
A[] = {1,1,3}
Output: 0
Explanation: no such sub-sequence exist.
Your Task:
Your task is to complete the function find3Numbers which finds any 3 elements in it such that A[i] < A[j] < A[k] and i < j < k. You need to return them as a vector/ArrayList/array (depending on the language cpp/Java/Python), if no such element is present then return the empty vector of size 0.
Note: The output will be 1 if the sub-sequence returned by the function is present in array A or else 0. If the sub-sequence returned by the function is not in the format as mentioned then the output will be -1.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 10^{5}
1 <= A[i] <= 10^{6}, for each valid i
"""

def find_3_numbers(A, n):
    if n < 3:
        return []
    
    mina = [-1] * n
    maxa = [-1] * n
    min_ = 0
    max_ = n - 1
    
    # Fill mina array
    for i in range(1, n):
        if A[i] <= A[min_]:
            mina[i] = -1
            min_ = i
        else:
            mina[i] = min_
    
    # Fill maxa array
    for i in range(n - 2, -1, -1):
        if A[i] >= A[max_]:
            maxa[i] = -1
            max_ = i
        else:
            maxa[i] = max_
    
    # Find the triplet
    for i in range(n):
        if mina[i] != -1 and maxa[i] != -1:
            return [A[mina[i]], A[i], A[maxa[i]]]
    
    return []