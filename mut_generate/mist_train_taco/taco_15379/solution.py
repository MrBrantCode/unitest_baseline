"""
QUESTION:
Given an array of n integers(duplicates allowed). Print “Yes” if it is a set of contiguous integers else print “No”.
Example 1:
Ã¢â¬â¹Input : arr[ ] = {5, 2, 3, 6, 4, 4, 6, 6}
Output : Yes
Explanation:
The elements  of array form a contiguous 
set of integers which is {2, 3, 4, 5, 6} 
so the output is "Yes".
Example 2:
Input : arr[ ] = {10, 14, 10, 12, 12, 
                              13, 15} 
Output : No
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function areElementsContiguous() that takes an array (arr), sizeOfArray (n), and return the true if it is a set of contiguous integers else print false. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
CONSTRAINTS:
1 ≤ N ≤10^{5}
1 ≤ a[i] ≤ 10^{5}
"""

def are_elements_contiguous(arr, n):
    num_set = set(arr)
    minimum = min(num_set)
    maximum = max(num_set)
    expected_count = maximum - minimum + 1
    return len(num_set) == expected_count