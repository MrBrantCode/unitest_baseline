"""
QUESTION:
Given an array of integers of size N. For each ith element in the array, calculate the absolute difference between the count of numbers that are to the left of i and are strictly greater than ith element, and the count of numbers that are to the right of i and are strictly lesser than ith element.
Example 1:
Input:
N = 5
A[] = {5, 4, 3, 2, 1}
Output: 4 2 0 2 4 
Explanation: We can see that the 
required number for the 
1st element is |0-4| = 4
Example 2:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output: 0 0 0 0 0
Explanation: There is no greater 
element on the left for any element 
and no lesser element on the right.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function greaterLesser() which takes the array arr[], its size Nas input parameters and returns the required array.
Expected Time Complexity: O(N log N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
-10^{9}^{ }≤ arr[i] ≤ 10^{9}
Array can contain duplicate elements.
"""

from bisect import bisect, bisect_left

def calculate_greater_lesser_diff(arr, N):
    output = []
    left = []
    
    # Calculate the count of numbers greater than the current element on the left
    for item in arr:
        i = bisect(left, item)
        output.append(len(left) - i)
        left.insert(i, item)
    
    right = []
    
    # Calculate the count of numbers less than the current element on the right
    for (i, item) in enumerate(arr[::-1]):
        j = bisect_left(right, item)
        right.insert(j, item)
        output[-i - 1] = abs(output[-i - 1] - j)
    
    return output