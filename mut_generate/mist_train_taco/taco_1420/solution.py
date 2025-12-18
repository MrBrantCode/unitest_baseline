"""
QUESTION:
Given an array arr of n integers, task is to print the array in the order – smallest number, largest number, 2nd smallest number, 2nd largest number, 3rd smallest number, 3rd largest number and so on.
Example 1:
Input:
n = 9
arr[] = {1, 9, 2, 8, 3, 7, 4, 6, 5}
Output:
1 9 2 8 3 7 4 6 5
Explanation:
Smallest number is 1. Largest number is 9. 
2nd smallest number is 2. Then 2nd largest
number is 8. And so on.
Example 2:
Input:
n = 4
arr[] = {1, 2, 3, 4}
Output:
1 4 2 3
Your Task:
You don't need to read input or print anything. Your task is to complete the function rearrangeArray() which takes the array of integers arr and n as parameters and returns void. You need to change the array itself.
Expected Time Complexity: O(n*logn)
Expected Auxiliary Space: O(n)
Constraints: 
1 <= n <= 10^{5}
1 <= arr[i] <=10^{6}
"""

def rearrange_array(arr, n):
    result = []
    arr.sort()
    left = 0
    right = n - 1
    while left < right:
        result.append(arr[left])
        result.append(arr[right])
        left += 1
        right -= 1
    if n % 2 == 1:
        result.append(arr[left])
    for i in range(n):
        arr[i] = result[i]