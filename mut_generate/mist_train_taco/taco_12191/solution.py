"""
QUESTION:
Given an array of integers a of length n and a value k. You have to find out the maximum possible numbers within 10^{9}whose sum does not exceed k  but are not present in the array.
Example 1:
Input: n = 4, 
       k = 14,
       a = {4, 6, 12, 8}
Output: 4
Explaination: The integers 1, 2, 3 and 5.
Example 2:
Input: n = 4,
       k = 25, 
       a = {5, 6, 7, 8}
Output: 5
Explaination: The integers are 1, 2, 3, 4 and 9.
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxNumbers() which takes n, k, and array as input parameters and returns the maximum number of integers that can be selected.
Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 10^{5}
1 ≤ a[i], k ≤ 10^{9}
"""

def max_numbers(n, k, a):
    e = 1
    s = set(a)
    r = 0
    while True:
        if e not in s:
            if k >= e:
                k -= e
                r += 1
            else:
                break
        e += 1
    return r