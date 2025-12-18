"""
QUESTION:
Given an array of distinct positive numbers, the task is to calculate the minimum number of subsets (or subsequences) from the array such that each subset contains consecutive numbers.
 
Example 1:
Input:
N = 10
Arr[] = {100, 56, 5, 6, 102, 58, 101, 57, 7, 103} 
Output:
3
Explanation:
{5, 6, 7}, { 56, 57, 58}, {100, 101, 102, 103} are
3 subset in which numbers are consecutive.
 
Example 2:
Input:
N = 3
Arr[] = {10, 100, 105}
Output:
3
Explanation:
{10}, {100} and {105} are 3 subset
in which numbers are consecutive.
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function numofsubset() which takes the array Arr[] and its size N as inputs and returns the count of number of such subset's that contains consecutive numbers.
 
Expected Time Complexity: O(N. log(N))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N≤ 10^{5}
1 ≤ A[] ≤ 10^{5}
"""

def count_consecutive_subsets(arr, n):
    # Sort the array
    arr.sort()
    
    # Initialize the count of subsets
    subsets = 1
    
    # Iterate through the array to count subsets
    i = 0
    while i < n - 1:
        if arr[i + 1] != arr[i] + 1:
            subsets += 1
        i += 1
    
    return subsets