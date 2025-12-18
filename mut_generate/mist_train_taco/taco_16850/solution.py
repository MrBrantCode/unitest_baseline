"""
QUESTION:
Given an array a[ ] of N elements. Consider array as a circular array i.e. element after a_{n} is a_{1}. The task is to find maximum sum of the absolute difference between consecutive elements with rearrangement of array elements allowed i.e. after any rearrangement of array elements find |a_{1} – a_{2}| + |a_{2} – a_{3}| + …… + |a_{n-1 }– a_{n}| + |a_{n} – a_{1}|.
Example 1:
Input:
N = 4
a[] = {4, 2, 1, 8}
Output: 
18
Explanation: Rearrangement done is {1, 8, 
2, 4}. Sum of absolute difference between 
consecutive elements after rearrangement = 
|1 - 8| + |8 - 2| + |2 - 4| + |4 - 1| = 
7 + 6 + 2 + 3 = 18.
Example 2:
Input:
N = 2
a[] = {10, 12}
Output: 
4
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function maxSum() that takes array a[ ] and its size N as input parameters and return the maximum sum using above method.
Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(1)
Constraints:
2 ≤ N ≤ 10^{5}
"""

def calculate_max_sum_of_absolute_differences(arr, n):
    # Sort the array
    arr = sorted(arr)
    
    # Initialize pointers
    i, j = 0, n - 1
    
    # Initialize the result list
    result = []
    
    # Fill the result list with elements in a specific order
    while i < j:
        result.append(arr[i])
        result.append(arr[j])
        i += 1
        j -= 1
    
    # If the array length is odd, append the middle element
    if i == j:
        result.append(arr[i])
    
    # Calculate the final sum of absolute differences
    final_sum = 0
    for i in range(1, n):
        final_sum += abs(result[i] - result[i - 1])
    
    # Add the circular difference
    final_sum += abs(result[-1] - result[0])
    
    return final_sum