"""
QUESTION:
Given an array nums of n elements and q queries . Each query consists of two integers l and r . You task is to find the number of elements of nums[] in range [l,r] which occur atleast k times.
 
Example 1:
Input: nums = {1,1,2,1,3}, Queries = {{1,5},
{2,4}}, k = 1
Output: {3,2}
Explanation: For the 1st query, from l=1 to r=5
1, 2 and 3 have the frequency atleast 1.
For the second query, from l=2 to r=4, 1 and 2 have 
the frequency atleast 1.
 
Example 1:
Input: nums = {1,2,3,1}, Queries = {{1,4},
{2,4},{4,4}, k = 2
Output: {1,0,0}
Explanation: For the 1st query, from l=1 to r=4
1 have the frequency atleast 2.
For the second query, from l=2 to r=4, no number has 
the frequency atleast 2.
For the third query, from l=4 to r=4, no number has 
the frequency atleast 2.
 
Your Task:
Your task is to complete the function solveQueries() which takes nums, Queries and k as input parameter and returns a list containg the answer for each query.
 
Expected Time Complexity: O(n*sqrt(n)*log(n))
Expected Space Compelxity: O(n)
 
Constraints:
1 <= n, no of Queries, k <= 10^{4}
1 <= nums[i] <= 10^{3}
1 <= Queries[i][0] <= Queries[i][1] <= n
"""

import math

def solve_queries(nums, queries, k):
    answers = [0] * len(queries)
    count = {}
    n = int(math.sqrt(len(nums))) + 1
    q = list(enumerate(queries))
    q.sort(key=lambda a: [int(a[1][0] / n), -a[1][1]])
    currentL = 0
    currentR = -1
    ans = 0
    
    for i in q:
        left = i[1][0] - 1
        right = i[1][1] - 1
        
        while currentR < right:
            currentR += 1
            count[nums[currentR]] = count.get(nums[currentR], 0) + 1
            if count[nums[currentR]] == k:
                ans += 1
        
        while currentL < left:
            count[nums[currentL]] -= 1
            if count[nums[currentL]] == k - 1:
                ans -= 1
            currentL += 1
        
        while currentR > right:
            count[nums[currentR]] -= 1
            if count[nums[currentR]] == k - 1:
                ans -= 1
            currentR -= 1
        
        while currentL > left:
            currentL -= 1
            count[nums[currentL]] = count.get(nums[currentL], 0) + 1
            if count[nums[currentL]] == k:
                ans += 1
        
        answers[i[0]] = ans
    
    return answers