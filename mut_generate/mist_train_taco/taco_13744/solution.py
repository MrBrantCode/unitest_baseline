"""
QUESTION:
Given two sorted arrays array1 and array2 of size m and n respectively. Find the median of the two sorted arrays.
Example 1:
Input:
m = 3, n = 4
array1[] = {1,5,9}
array2[] = {2,3,6,7}
Output: 5
Explanation: The middle element for
{1,2,3,5,6,7,9} is 5
Example 2:
Input:
m = 2, n = 4
array1[] = {4,6}
array2[] = {1,2,3,5}
Output: 3.5
Your Task:
The task is to complete the function MedianOfArrays() that takes array1 and array2 as input and returns their median. 
Can you solve the problem in expected time complexity?
Expected Time Complexity: O(min(log n, log m)).
Expected Auxiliary Space: O((n+m)/2).
Constraints: 
0 ≤ m,n ≤ 10^{6}
1 ≤ array1[i], array2[i] ≤ 10^{9}
"""

def find_median_of_two_sorted_arrays(array1, array2):
    n1, n2 = len(array1), len(array2)
    total = n1 + n2
    half = total // 2
    
    if n2 < n1:
        return find_median_of_two_sorted_arrays(array2, array1)
    
    l, r = 0, n1 - 1
    
    while True:
        i = (l + r) // 2
        j = half - i - 2
        
        left_1 = array1[i] if i >= 0 else float('-inf')
        right_1 = array1[i + 1] if (i + 1) < n1 else float('inf')
        left_2 = array2[j] if j >= 0 else float('-inf')
        right_2 = array2[j + 1] if (j + 1) < n2 else float('inf')
        
        if left_1 <= right_2 and left_2 <= right_1:
            if total % 2 == 0:
                sum_values = max(left_1, left_2) + min(right_1, right_2)
                return sum_values / 2
            else:
                return min(right_1, right_2)
        elif left_1 > right_2:
            r = i - 1
        else:
            l = i + 1