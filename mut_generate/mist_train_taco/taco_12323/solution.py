"""
QUESTION:
Given an array Arr of size N, swap the K_{th} element from beginning with K_{th} element from end.
Example 1:
Input:
N = 8, K = 3
Arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: 1 2 6 4 5 3 7 8
Explanation: K_{th} element from beginning is
3 and from end is 6.
Example 2:
Input:
N = 5, K = 2
Arr[] = {5, 3, 6, 1, 2}
Output: 5 1 6 3 2
Explanation: K_{th} element from beginning is
3 and from end is 1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function swapKth() which takes the array of integers arr, n and k as parameters and returns void. You have to modify the array itself.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ K ≤ N ≤ 10^{5}
1 ≤ Arr[i] ≤ 10^{3}
"""

def swap_kth_elements(arr, n, k):
    # Swap the Kth element from the beginning with the Kth element from the end
    arr[k - 1], arr[-k] = arr[-k], arr[k - 1]