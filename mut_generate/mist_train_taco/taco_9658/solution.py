"""
QUESTION:
Given an array of integers arr[] of length N, every element appears thrice except for one which occurs once.
Find that element which occurs once.
Example 1:
Input:
N = 4
arr[] = {1, 10, 1, 1}
Output:
10
Explanation:
10 occurs once in the array while the other
element 1 occurs thrice.
Example 2:
Input:
N = 10
arr[] = {3, 2, 1, 34, 34, 1, 2, 34, 2, 1}
Output:
3
Explanation:
All elements except 3 occurs thrice in the array.
 
Your Task:
The task is to complete the function singleElement() which finds and returns the element occuring once in the array.
Constraints:
1 ≤ N ≤ 10^{6}
-10^{9} ≤ A[i] ≤ 10^{9}
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
"""

from collections import Counter

def find_single_element(arr, N):
    # Create a counter object to count occurrences of each element
    count = Counter(arr)
    
    # Iterate through the counter to find the element that occurs only once
    for element, frequency in count.items():
        if frequency == 1:
            return element