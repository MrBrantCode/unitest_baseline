"""
QUESTION:
Given an unsorted array arr[] of n positive integers. Find the number of triangles that can be formed with three different array elements as lengths of three sides of triangles. 
Example 1:
Input: 
n = 3
arr[] = {3, 5, 4}
Output: 
1
Explanation: 
A triangle is possible 
with all the elements 5, 3 and 4.
Example 2:
Input: 
n = 5
arr[] = {6, 4, 9, 7, 8}
Output: 
10
Explanation: 
There are 10 triangles
possible  with the given elements like
(6,4,9), (6,7,8),...
 
Your Task: 
This is a function problem. You only need to complete the function findNumberOfTriangles() that takes arr[] and n as input parameters and returns the count of total possible triangles.
Expected Time Complexity: O(n^{2}).
Expected Space Complexity: O(1).
Constraints:
3 <= n <= 10^{3}
1 <= arr[i] <= 10^{3}
"""

def count_possible_triangles(arr, n):
    # Sort the array
    arr.sort()
    
    # Initialize the count of triangles
    count = 0
    
    # Iterate over the array from the end to the beginning
    for i in range(n - 1, 1, -1):
        left = 0
        right = i - 1
        
        # Use two pointers to find valid triangles
        while left < right:
            if arr[left] + arr[right] > arr[i]:
                count += right - left
                right -= 1
            else:
                left += 1
    
    return count