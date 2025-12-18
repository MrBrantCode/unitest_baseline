"""
QUESTION:
Given an array A of N elements. The task is to find the greatest number S such that it is product of two elements of given array (S cannot be included in pair. Also, pair must be from different indices). 
Example 1:
Input :  arr[] = {10, 3, 5, 30, 35}
Output:  30
Explanation: 30 is the product of 10 and 3.
Example 2:
Input :  arr[] = {2, 5, 7, 8}
Output:  -1
Explanation: Since, no such element exists.
Example 3:
Input  :  arr[] = {10, 2, 4, 30, 35}
Output:  -1
 
Example 4:
Input :  arr[] = {10, 2, 2, 4, 30, 35}
Output:  4
Example 5:
Input  : arr[] = {17, 2, 1, 35, 30}
Output : 35
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findGreatest() which takes the array arr[] and its size N as inputs and returns the answer. If the answer is not present in the array, return -1.
Expected Time Complexity: O(N. Log(N))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{6}
1 ≤ A_{i} ≤ 10^{7}
"""

def find_greatest_product_pair(arr, n):
    m = dict()
    for i in arr:
        m[i] = m.get(i, 0) + 1
    arr = sorted(arr)
    for i in range(n - 1, 0, -1):
        j = 0
        if arr[i] == 1:
            if m[1] > 2:
                return 1
            continue
        while j < i and arr[j] <= sqrt(arr[i]):
            if arr[j] == 1:
                if m[arr[i]] > 1:
                    return arr[i]
                j += 1
                continue
            if arr[i] % arr[j] == 0:
                result = arr[i] // arr[j]
                if result != arr[j] and result in m.keys() and (m[result] > 0):
                    return arr[i]
                elif result == arr[j] and result in m.keys() and (m[result] > 1):
                    return arr[i]
            j += 1
    return -1