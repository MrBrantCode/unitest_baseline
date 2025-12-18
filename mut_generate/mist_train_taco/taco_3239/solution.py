"""
QUESTION:
Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
Example 1:
Input: 
n = 4, arr1[] = [1 3 5 7] 
m = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
Explanation:
After merging the two 
non-decreasing arrays, we get, 
0 1 2 3 5 6 7 8 9.
Example 2:
Input: 
n = 2, arr1[] = [10 12] 
m = 3, arr2[] = [5 18 20]
Output: 
arr1[] = [5 10]
arr2[] = [12 18 20]
Explanation:
After merging two sorted arrays 
we get 5 10 12 18 20.
Your Task:
You don't need to read input or print anything. You only need to complete the function merge() that takes arr1, arr2, n and m as input parameters and modifies them in-place so that they look like the sorted merged array when concatenated.
Expected Time Complexity:  O((n+m) log(n+m))
Expected Auxilliary Space: O(1)
Constraints:
1 <= n, m <= 10^{5}
0 <= arr1_{i}, arr2_{i} <= 10^{7}
"""

def merge_sorted_arrays(arr1, arr2, n, m):
    """
    Merges two sorted arrays arr1 and arr2 of sizes n and m respectively,
    without using any extra space. Modifies arr1 to contain the first N
    elements and arr2 to contain the last M elements in sorted order.

    Parameters:
    arr1 (list): The first sorted array of size n.
    arr2 (list): The second sorted array of size m.
    n (int): The size of the first array arr1.
    m (int): The size of the second array arr2.

    Returns:
    None: The function modifies arr1 and arr2 in-place.
    """
    left = n - 1
    right = 0
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break
    arr1.sort()
    arr2.sort()