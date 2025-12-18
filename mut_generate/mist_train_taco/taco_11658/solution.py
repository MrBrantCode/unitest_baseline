"""
QUESTION:
Given an array and two integers say, x and y, find the number of sub-arrays in which the number of occurrences of x is equal to number of occurrences of y.
Example 1:
Input:
n = 4, x = 1, y = 2
arr[] = {1, 2, 1}
Output: 2
Explanation:
The possible sub-arrays have same equal 
number of occurrences of x and y are:
1) {1, 2}, x and y have same occurrence(1).
2) {2, 1}, x and y have same occurrence(1).
Example 2:
Input:
n = 5, x = 4, y = 6
arr[] = {1, 2, 1}
Output: 6
Explanation:
The possible sub-arrays have same equal 
number of occurrences of x and y are:
1) {1}, x and y have same occurrence(0).
2) {2}, x and y have same occurrence(0).
3) {1}, x and y have same occurrence(0).
4) {1, 2}, x and y have same occurrence(0).
5) {2, 1}, x and y have same occurrence(0).
6) {1, 2, 1}, x and y have same occurrence(0).
Your Task:
You don't need to read input or print anything. Your task is to complete the function sameOccurrence() which takes the array of integers arr, n, x and y as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
Constraints: 
1 <= n <= 10^{5}
1 <= arr[i], x, y<=10^{6}
"""

def count_subarrays_with_same_occurrence(arr, x, y):
    n = len(arr)
    if x == y:
        return n * (n + 1) // 2
    
    diff = 0
    diff_to_count = {0: 1}
    ans = 0
    
    for num in arr:
        if num == x:
            diff += 1
        elif num == y:
            diff -= 1
        
        if diff in diff_to_count:
            ans += diff_to_count[diff]
        
        if diff not in diff_to_count:
            diff_to_count[diff] = 0
        
        diff_to_count[diff] += 1
    
    return ans