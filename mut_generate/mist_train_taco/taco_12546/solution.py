"""
QUESTION:
Given an array A[ ] your task is to complete the function max_val which finds the maximum value of abs(i – j) * min(arr[i], arr[j]) where i and j vary from 0 to n-1. 
Example 1:
Input:
N = 4
arr[] = 3 2 1 4
Output: 9
Explanation:
Here, a[0] = 3 and a[3] = 4 
and thus result is  
abs(0-3)*min(3,4) = 9.
Example 2:
Input:
N= 4
arr[] = 8 1 9 4
Output: 16
Explanation:
Here, a[0]=8 and a[2]=9 thus 
result is abs(0-2)*min(8,9)=16. 
Your task:
You don't need to read input or print anything. Your task is to complete the function max_val() which takes the array and it's size as input and returns the maximum value of abs(i – j) * min(arr[i], arr[j]).
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1<=N<=10^4
-10^5<=A[]<=10^5
"""

def max_val(arr, n):
    lst = []
    i = 0
    j = n - 1
    while i < j:
        p = abs(i - j) * min(arr[i], arr[j])
        lst.append(p)
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
    return max(lst)