"""
QUESTION:
Given an array, the task is to print K smallest elements from the array but they must be in the same order as they are in a given array.
Example 1:
 
Input : A[] = {1, 2, 2, 3, 1} and K = 2
Output : 1 1
Explanation:
In an array A[] = {1, 2, 2, 3, 1} the smallest
element is 1 and the second smallest element 
is also 1. So, we will return [1, 1] as an 
answer.
Example 2:
Input : A[] = {1, 4, 3, 3, 5, 5} and K = 2
Output : 1 3
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function kSmallestElements() that takes an array (arr), sizeOfArray (n), element (K) and return the array of K smallest element. The driver code takes care of the printing.
Expected Time Complexity: O(N*LOG(N)).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ K ≤ N ≤ 10^{6}
1 ≤ A[i] ≤ 10^{5}
"""

def k_smallest_elements(arr, k):
    # Create a dictionary to map indices to their corresponding values
    index_value_map = {i: arr[i] for i in range(len(arr))}
    
    # Sort the dictionary items by value to get the smallest elements
    sorted_items = sorted(index_value_map.items(), key=lambda x: x[1])[:k]
    
    # Extract the values from the sorted items and sort them by their original indices
    result = [item[1] for item in sorted(sorted_items, key=lambda x: x[0])]
    
    return result