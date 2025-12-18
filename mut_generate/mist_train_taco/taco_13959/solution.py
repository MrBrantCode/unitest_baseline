"""
QUESTION:
The chef has one array of N natural numbers (might be in sorted order). Cheffina challenges chef to find the total number of inversions in the array.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains two lines of input, $N$.
- N space-separated natural numbers. 

-----Output:-----
For each test case, output in a single line answer as the total number of inversions.

-----Constraints-----
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq arr[i] \leq 10^5$

-----Sample Input:-----
1
5
5 4 1 3 2

-----Sample Output:-----
8
"""

def count_inversions(arr):
    def mergeSort(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2
            inv_count += mergeSort(arr, temp_arr, left, mid)
            inv_count += mergeSort(arr, temp_arr, mid + 1, right)
            inv_count += merge(arr, temp_arr, left, mid, right)
        return inv_count

    def merge(arr, temp_arr, left, mid, right):
        i = left
        j = mid + 1
        k = left
        inv_count = 0
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += mid - i + 1
                k += 1
                j += 1
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]
        return inv_count

    n = len(arr)
    temp_arr = [0] * n
    return mergeSort(arr, temp_arr, 0, n - 1)