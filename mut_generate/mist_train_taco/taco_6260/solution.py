"""
QUESTION:
Given an array where every element appears twice except a pair (two elements). return the elements of this unique pair in sorted order.
 
Example 1:
Input : Arr[] = {2, 2, 5, 5, 6, 7}
Output : 6 7
Explanation:
We can see we have [2, 2, 5, 5, 6, 7]. 
Here 2 and 5 are coming two times. 
So, the answer will be 6 7.
Example 2:
Input : Arr[] = {1, 3, 4, 1}
Output : 3 4
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function findUniquePair() that takes an array (arr), sizeOfArray (n) and return the unique pair's element in increasing order. The driver code takes care of the printing.
 
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{7}
"""

from collections import Counter

def find_unique_pair(arr, n):
    # Count the frequency of each element in the array
    frequency = Counter(arr)
    
    # Find the unique elements (elements with frequency 1)
    unique_elements = [item for item, count in frequency.items() if count == 1]
    
    # Sort the unique elements
    unique_elements.sort()
    
    # Return the sorted unique elements
    return unique_elements