"""
QUESTION:
Given an unsorted array Arr of length N. Your task is to find the maximum difference between the successive elements in its sorted form.
Return 0 if the array contains less than 2 elements.
Example 1:
Input:
N = 3
Arr[] = {1, 10, 5}
Output: 5
Explanation: The maximum difference
between  successive elements of array
is 5(abs(5-10)).
Your Task:
Complete the function maxSortedAdjacentDiff() which takes array arr and size n, as input parameters and returns an integer representing the answer. You don't to print answer or take inputs.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
1 ≤ Arr[i] ≤ 10^{6}
"""

def max_sorted_adjacent_diff(arr, n):
    # If the array contains less than 2 elements, return 0
    if n < 2:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize the maximum difference to 0
    max_diff = 0
    
    # Iterate through the sorted array to find the maximum difference
    for i in range(1, n):
        max_diff = max(max_diff, arr[i] - arr[i - 1])
    
    # Return the maximum difference found
    return max_diff