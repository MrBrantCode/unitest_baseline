"""
QUESTION:
Given two arrays of length N and M, print the merged array in ascending order containing only unique elements.
Example 1:
Input:
N = 2
a[] = {1, 8}
M = 2
b[] = {10, 11}
Output:
answer[] = {1, 8, 10, 11}
Explanation:
The answer[] array after merging both
the arrays and removing duplicates is
[1 8, 10, 11]
You have to return the size of the array
formed ( 4 in this case) and update the
answer array in the function mergeNsort().
 
Example 2:
Input:
N = 5
a[] = {7, 1, 5, 3, 9}
M = 6
b[]  = {8, 4, 3, 5, 2, 6}
Output:
answer[] = {1, 2, 3, 4, 5, 6, 7, 8, 9} 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function mergeNsort() which takes the array A[], B[] and its size N, M respectively as inputs and returns the size of this array and store the merged array sorted in ascending order in the answer[].
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ M ≤ 10^{5}
1 ≤ A_{i} ≤ 10^{5}
1 ≤ B_{i} ≤ 10^{5}
"""

def merge_and_sort_unique(a, b, n, m, answer):
    # Merge both arrays and convert to a set to remove duplicates
    merged_set = set(a + b)
    
    # Sort the unique elements and store them in the answer list
    answer[:] = sorted(merged_set)
    
    # Return the size of the merged and sorted array
    return len(answer)