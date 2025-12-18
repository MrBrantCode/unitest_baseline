"""
QUESTION:
Given an unsorted array of integers. Find an element such that all the elements to its left are smaller and to its right are greater. Print -1 if no such element exists. Note that there can be more than one such element. In that case print the first such number occurring in the array.
Example 1:
Input: N = 7, arr[] = {4, 3, 2, 5, 8, 6, 7} 
Output: 5
Explanation: To the left of element 5 
every element is smaller to it and to 
the right of element 5 every element 
is greater to it.  
Example 2:
Input: N = 7, arr[] = {5, 6, 2, 8, 10, 9, 8} 
Output: -1
Explanation: No such desired element is 
present in the array.
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function FindElement() that takes array arr and integer N as parameters and returns the desired output.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
"""

def find_element(arr, N):
    # Initialize an array to keep track of the maximum element on the left side
    left_max = [0] * N
    left_max[0] = arr[0]
    
    # Fill the left_max array
    for i in range(1, N):
        left_max[i] = max(left_max[i-1], arr[i])
    
    # Initialize the right_min to keep track of the minimum element on the right side
    right_min = [0] * N
    right_min[N-1] = arr[N-1]
    
    # Fill the right_min array
    for i in range(N-2, -1, -1):
        right_min[i] = min(right_min[i+1], arr[i])
    
    # Traverse the array to find the element
    for i in range(N):
        if left_max[i] <= arr[i] <= right_min[i]:
            return arr[i]
    
    # If no such element is found, return -1
    return -1