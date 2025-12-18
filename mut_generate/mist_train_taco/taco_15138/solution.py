"""
QUESTION:
A step array is an array of integers where each element has a difference of at most k with its neighbor. Given a key x, we need to find the index value of x if multiple elements exist, and return the first occurrence of the key. 
Example 1:
Input : arr[ ] = {4, 5, 6, 7, 6}, K = 1 
        and X = 6
Output : 2
Explanation:
In an array arr 6 is present at index 2.
So, return 2.
Example 2:
Input : arr[ ] = {20 40 50}, K = 20 
        and X = 70
Output :  -1 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function search() that takes an array (arr), sizeOfArray (n), an integer value X, another integer value K, and return an integer displaying the index of the element X in the array arr. If the element is not present in the array return -1. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ K ≤ 10^{2}
1 ≤ arr[i], X ≤ 10^{5}
"""

def find_first_occurrence(arr, x, k):
    """
    Finds the index of the first occurrence of the key `x` in the array `arr`
    where each element has a difference of at most `k` with its neighbor.

    Parameters:
    arr (list of int): The array of integers.
    x (int): The key value to search for.
    k (int): The maximum difference allowed between consecutive elements.

    Returns:
    int: The index of the first occurrence of `x` in `arr`, or -1 if not found.
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1