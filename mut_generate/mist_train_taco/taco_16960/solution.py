"""
QUESTION:
Given a positive integer n, generate all possible unique ways to represent n as sum of positive integers.
Note: The generated output is printed without partitions. Each partition must be in decreasing order. Printing of all the partitions is done in reverse sorted order. 
Example 1:
Input: n = 3
Output: 3 2 1 1 1 1
Explanation: For n = 3, 
{3}, {2, 1} and {1, 1, 1}.
 
Example 2:
Input: n = 4 
Output: 4 3 1 2 2 2 1 1 1 1 1 1
Explanation: For n = 4, 
{4}, {3, 1}, {2, 2}, {2, 1, 1}, {1, 1, 1, 1}.
Your Task:
You don't need to read or print anything. Your task is to complete the function UniquePartitions() which takes n as input parameter and returns a list of all possible combinations in lexicographically decreasing order. 
 
Expected Time Complexity: O(2^n)
Expected Space Complexity: O(n)
 
Constraints:
1 <= n <= 25
"""

def generate_unique_partitions(n):
    def util(a, n, S, s):
        nonlocal ans
        if S == 0:
            s = s[:-1]
            s = s.split(',')
            ans.append(s)
            return
        if n == 0:
            return
        if a[n - 1] <= S:
            util(a, n, S - a[n - 1], s + str(a[n - 1]) + ',')
            util(a, n - 1, S, s)
        else:
            util(a, n - 1, S, s)

    ans = []
    a = [i for i in range(1, n + 1)]
    util(a, n, n, '')
    return ans