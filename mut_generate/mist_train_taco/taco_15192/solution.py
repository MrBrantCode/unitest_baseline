"""
QUESTION:
Given an array arr[] of length n. Find all possible unique permutations of the array.
Example 1:
Input: 
n = 3
arr[] = {1, 2, 1}
Output: 
1 1 2
1 2 1
2 1 1
Explanation:
These are the only possible unique permutations
for the given array.
Example 2:
Input: 
n = 2
arr[] = {4, 5}
Output: 
4 5
5 4
Your Task:
You don't need to read input or print anything. You only need to complete the function uniquePerms() that takes an integer n, and an array arr of size n as input and returns a sorted list of lists containing all unique permutations of the array.
Expected Time Complexity:  O(n*n!)
Expected Auxilliary Space: O(n*n!)
 
Constraints:
1 ≤ n ≤ 9
1 ≤ arr_{i} ≤ 10
"""

def unique_permutations(arr, n):
    def permutations(s, n, ans, subs, freq, k):
        if k == n:
            ans.append(subs[:])
            return
        i = 0
        while i < n:
            if i != 0 and s[i] == s[i - 1] and (freq[i - 1] == 0):
                i += 1
                continue
            if freq[i] == 0:
                subs.append(s[i])
                freq[i] = 1
                k += 1
                permutations(s, n, ans, subs, freq, k)
                k -= 1
                freq[i] = 0
                subs.pop()
            i += 1

    arr.sort()
    ans = []
    subs = []
    freq = [0] * n
    k = 0
    permutations(arr, n, ans, subs, freq, k)
    return ans