"""
QUESTION:
You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.
Example 1:
Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
Example 2:
Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
Your Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 <= N <= 10^{6}
-10^{6} <= arr[i] <= 10^{6}
"""

def find_smallest_missing_positive(arr, n):
    # Create a dictionary to track the presence of positive numbers
    d = {}
    
    # Initialize the dictionary with keys from 1 to the maximum value in arr
    for i in range(1, max(arr) + 1):
        d[i] = 0
    
    # Mark the presence of positive numbers in the dictionary
    for i in arr:
        if i > 0:
            d[i] += 1
    
    # Find the first missing positive number
    for key, value in d.items():
        if value == 0:
            return key
    
    # If all positive numbers are present, return the next positive number
    return max(arr) + 1