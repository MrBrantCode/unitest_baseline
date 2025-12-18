"""
QUESTION:
Given an array arr[] of integers of size N that might contain duplicates, the task is to find all possible unique subsets.
Note: Each subset should be sorted.
Example 1:
Input: N = 3, arr[] = {2,1,2}
Output:(),(1),(1 2),(1 2 2),(2),(2 2)
Explanation: 
All possible subsets = (),(2),(1),(1,2),(2),(2,2),(2,1),(2,1,2)
After Sorting each subset = (),(2),(1),(1,2),(2),(2,2),(1,2),(1,2,2) 
Unique Susbsets in Lexicographical order = (),(1),(1,2),(1,2,2),(2),(2,2)
Example 2:
Input: N = 4, arr[] = {1,2,3,3}
Output: (),(1),(1 2),(1 2 3)
(1 2 3 3),(1 3),(1 3 3),(2),(2 3)
(2 3 3),(3),(3 3)
Your Task:
Your task is to complete the function AllSubsets() which takes the array arr[] and N as input parameters and returns list of all possible unique subsets in lexicographical order. 
Expected Time Complexity: O(2^{N}).
Expected Auxiliary Space: O(2^{N} * X), X = Length of each subset.
Constraints:
1 ≤ N ≤ 12
1 ≤ arr[i] ≤ 9
"""

def generate_unique_subsets(arr, n):
    def solve(s, ou, res):
        if len(s) == 0:
            res.add(tuple(ou))
            return
        ou1 = ou[:]
        ou2 = ou[:]
        ou2.append(s[0])
        s = s[1:]
        solve(s, ou1, res)
        solve(s, ou2, res)

    ou = []
    res = set()
    arr.sort()
    solve(arr, ou, res)
    res = list(res)
    res.sort()
    return res