"""
QUESTION:
Given an array arr[] of N integers, calculate the median
 
Example 1:
Input: N = 5
arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array 
middle element is the median 
Example 2:
Input: N = 4
arr[] = 56 67 30 79
Output: 61
Explanation: In case of even number of 
elements, average of two middle elements 
is the median.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function find_median() which takes the array as input parameter and returns the floor value of the median.
 
Expected Time Complexity: O(n * log(n))
Expected Space Complexity: O(1)
 
Constraints:
1 <= Length of Array <= 100
1 <= Elements of Array <= 100
"""

def calculate_median(arr):
    n = len(arr)
    if n == 0:
        return -1
    
    arr.sort()
    
    if n % 2 == 0:
        p1 = n // 2
        p2 = p1 - 1
        return (arr[p1] + arr[p2]) // 2
    else:
        return arr[n // 2]