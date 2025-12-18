"""
QUESTION:
Given an array containing n numbers. The problem is to find the length of the longest contiguous subarray such that every element in the subarray is strictly greater than its previous element in the same subarray.
 
Example 1:
Input:
n = 9
a[] = {5, 6, 3, 5, 7, 8, 9, 1, 2}
Output:
5
 
Example 2:
Input:
n = 10
a[] = {12, 13, 1, 5, 4, 7, 8, 10, 10, 11}
Output:
4
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function lenOfLongIncSubArr() which takes the array a[] and its size n as inputs and returns the length of the longest increasing subarray.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
 
Constraints: 
1<=n<=10^{5}
1<=a[i]<=10^{5}
"""

def len_of_longest_increasing_subarray(a, n):
    if n == 0:
        return 0
    
    current_length = 1
    max_length = 1
    
    for i in range(1, n):
        if a[i] > a[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    
    max_length = max(max_length, current_length)
    return max_length