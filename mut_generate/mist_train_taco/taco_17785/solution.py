"""
QUESTION:
Given two arrays of equal size N and an integer K. The task is to check if after permuting both arrays, we get sum of their corresponding element greater than or equal to k i.e A_{i} + B_{i} >= K for all i (from 0 to N-1). Return true if possible, else false.
 
Example 1:
Input : 
a[] = {2, 1, 3}, 
b[] = { 7, 8, 9 }, 
k = 10. 
Output : 
True
Explanation:
Permutation  a[] = { 1, 2, 3 } 
and b[] = { 9, 8, 7 } 
satisfied the condition a[i] + b[i] >= K.
 
Example 2:
Input : 
a[] = {1, 2, 2, 1}, b[] = { 3, 3, 3, 4 }, k = 5.
Output : 
False
Explanation:
Since any permutation won't give the answer.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isPossible() which takes the array A[], B[], its size N and an integer K as inputs and returns the answer.
Expected Time Complexity: O(N. Log(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ K ≤ 10^{18 }
1 ≤ A_{i}, B_{i} ≤ 10^{17}
"""

def is_possible_permutation(a, b, k):
    # Sort array a in ascending order
    a.sort()
    # Sort array b in descending order
    b.sort(reverse=True)
    
    # Check if the sum of corresponding elements is >= k
    for i in range(len(a)):
        if a[i] + b[i] < k:
            return False
    
    return True