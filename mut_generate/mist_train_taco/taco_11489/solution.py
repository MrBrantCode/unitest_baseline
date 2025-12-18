"""
QUESTION:
Given an array of integers. Find the Inversion Count in the array. 
Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 
Example 1:
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
Example 2:
Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already 
sorted so there is no inversion count.
Example 3:
Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array 
are same, so there is no inversion count.
Your Task:
You don't need to read input or print anything. Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.
Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).
Constraints:
1 ≤ N ≤ 5*10^{5}
1 ≤ arr[i] ≤ 10^{18}
"""

def inversion_count(arr, n):
    def merge(start, mid, end):
        len1, len2 = mid - start + 1, end - mid
        arr1 = [arr[ind] for ind in range(start, mid + 1)]
        arr2 = [arr[ind] for ind in range(mid + 1, end + 1)]
        i, j, k = 0, 0, start
        count = 0
        while i < len1 and j < len2:
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                count += len1 - i
                j += 1
            k += 1
        while i < len1:
            arr[k] = arr1[i]
            i += 1
            k += 1
        while j < len2:
            arr[k] = arr2[j]
            j += 1
            k += 1
        return count

    def merge_sort(start, end):
        count = 0
        if start < end:
            mid = start + (end - start) // 2
            l = merge_sort(start, mid)
            r = merge_sort(mid + 1, end)
            count = merge(start, mid, end) + l + r
        return count

    return merge_sort(0, n - 1)