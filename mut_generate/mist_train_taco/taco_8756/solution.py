"""
QUESTION:
Given an array arr[] of N integers, Geek wants to assign a value to each of the array elements. The minimum value that can be assigned to an element is 1. For every pair of adjacent elements, the one with the higher integral value should be assigned a higher value. Help Geek assign the smallest possible value to each element and find the sum of the values.
Example 1:
Input: 
N = 4
arr[] = {1, 2, 3, 4}
Output: 10
Explaination: First element is assigned value 1. 
Second element is assigned value 2 because 
arr[1]>arr[0].Third element is assigned value 3 
because arr[2]>arr[1]. Fourth element is assigned 
value 4 because arr[3]>arr[2]. 1+2+3+4 =10.
Example 2:
Input: 
N = 3
arr[] = {2, 4, 4}
Output: 4
Explaination: First element is assigned value 1.
Second element is assigned value 2 because 
arr[1]>arr[0]. Third element is assigned value 1 
because arr[2] is equal to arr[1]. 1+2+1 = 4.
Your Task:
You do not need to read input or print anything. Your task is to complete the function minValue() which takes N and arr[] as input parameters and returns the minimum possible sum.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 10^{5}
"""

def calculate_min_value_sum(arr):
    N = len(arr)
    output = [1] * N
    
    # Forward pass to assign initial values
    for i in range(N - 1):
        if arr[i] < arr[i + 1]:
            output[i + 1] = output[i] + 1
    
    # Backward pass to ensure values are correctly assigned
    for i in range(N - 1):
        if arr[-i - 1] < arr[-i - 2]:
            output[-i - 2] = max(output[-i - 2], output[-i - 1] + 1)
    
    return sum(output)