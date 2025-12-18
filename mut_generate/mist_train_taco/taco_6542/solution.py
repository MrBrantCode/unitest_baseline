"""
QUESTION:
Given an array A of non-negative integers. Sort the array in ascending order such that element at the Kth position in unsorted array stays unmoved and all other elements are sorted. 
Example 1:
Input:
N = 5, K = 2
arr[] = {3 12 30 79 2}
Output: 2 12 3 30 79
Explanation: The element at the 2nd 
position (12) remains at its own place 
while others are sorted.
Ã¢â¬â¹Example 2:
Input: 
N = 10, K = 5
arr[] = {16 16 18 10 9 22 11 5 35 22}
Output: 5 10 11 16 9 16 18 22 22 35
Explanation: The element at the 5th 
position (9) remains at its own place
while others are sorted.
Your Task:
You don't need to read input or print anything. Your task is to complete the function strangeSort() which takes the array A[], its size N and an integer K (1-based) as inputs and modifies the array such that all the elements except the one at the K-th position are sorted in non-decreasing order. The K-th position remains unchanged.
Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(1).
Constraints:
2<=N<=5*10^{5}
1<=K<=N
"""

def strange_sort(arr, n, k):
    # Extract the element at the k-th position (1-based index)
    kth_element = arr[k-1]
    
    # Sort the array excluding the k-th element
    sorted_arr = sorted(arr[:k-1] + arr[k:])
    
    # Reconstruct the array with the k-th element in its original position
    arr[:k-1] = sorted_arr[:k-1]
    arr[k-1] = kth_element
    arr[k:] = sorted_arr[k-1:]