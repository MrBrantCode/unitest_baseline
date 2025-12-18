"""
QUESTION:
Given an array of 0 and 1. In how many iterations it is possible that the whole array can be filled with 1's, if in a single iteration immediate neighbours of 1's can be filled.
 
Example 1:
Input:
n = 4
a[] = {1, 0, 1, 0}
Output:
1
Explanation:
Both the 0s has 1 as their immediate neighbour.
So, only one iteration is required to fill the
array with 1.
 
Example 2:
Input:
n = 5
a[] = {0, 0, 1, 0, 0}
Output:
2
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minMoves() which takes the array A[] and its size N as inputs and returns the minimum number of iterations to fill the whole array with 1's (if possible). If it is not possible to fill the array with 1s, return -1 . 
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{7}
0 <= A_{i }<= 1
"""

def min_iterations_to_fill_ones(arr, n):
    max_dist = -1
    last_one = -1
    
    for i in range(n):
        if arr[i] == 1:
            if last_one == -1:
                max_dist = i
            else:
                new_dist = i - last_one - 1
                max_dist = max(max_dist, (new_dist - 1) // 2 + 1)
            last_one = i
    
    if last_one != -1:
        final_dist = n - last_one - 1
        max_dist = max(max_dist, final_dist)
    
    return -1 if max_dist == -1 else max_dist