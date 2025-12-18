"""
QUESTION:
Given two sequences, one is increasing sequence a[] and another a normal sequence b[], find the K-th missing element in the increasing sequence which is not present in the given sequence. If no K-th missing element is there output -1
 
Example 1:
Input : Arr[] = {0, 2, 4, 6, 8, 10, 12, 14, 15}
Brr[] = {4, 10, 6, 8, 12} and K = 3
Output : 14
Explanation:
The numbers from increasing sequence that
are not present in the given sequence are 0, 2, 14, 15.
The 3rd missing number is 14.
Example 2:
Input : Arr[] = {1, 2, 3, 4, 5}
Brr[] = {5, 4, 3, 1, 2} and K = 3
Output : -1
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function MissingNumber() that takes an array (a), another array (b), an element K, size of first array (n), size of the second array (m), and return the Kth missing number in an array a, if you can't find it return -1. The driver code takes care of the printing.
Expected Time Complexity: O(n + m).
Expected Auxiliary Space: O(m).
Constraints:
1 ≤ n,m,k ≤ 10^{5}
1 ≤ a[i] ≤ 10^{8}
1 ≤ b[i] ≤ 10^{3}
"""

def find_kth_missing_element(a: list, b: list, k: int) -> int:
    # Convert list b to a set for O(1) average time complexity lookups
    b_set = set(b)
    
    # Counter for the missing elements
    missing_count = 0
    
    # Iterate through the increasing sequence a
    for num in a:
        if num not in b_set:
            missing_count += 1
            if missing_count == k:
                return num
    
    # If we exhaust the list and don't find the k-th missing element, return -1
    return -1