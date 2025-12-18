"""
QUESTION:
Given two positive integers x and y, and an array arr[] of positive integers. We need to find the longest prefix index which contains an equal number of x and y. Print the maximum index of largest prefix if exist otherwise print -1.
 
Example 1:
Input:
N=11
X=7  Y=42
arr[] = [ 7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7 ]
Output: 9
Explanation: The longest prefix with same 
number of occurrences of 7 and 42 is:
7, 42, 5, 6, 42, 8, 7, 5, 3, 6 
Example 2:
Input:
N=3
X=1 Y=2 
arr[] = [ 1,2,2 ]
Output: 1
Your Task:
Since this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function findIndex() that takes array arr, integer X, integer Y, and integer N as parameters and return the desired result.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
2 ≤ N ≤ 105
X != Y
"""

def find_longest_prefix_index(arr, X, Y, N):
    countx = 0
    county = 0
    index = -1
    
    for i in range(N):
        if arr[i] == X:
            countx += 1
        elif arr[i] == Y:
            county += 1
        
        if countx == county:
            index = i
    
    return index