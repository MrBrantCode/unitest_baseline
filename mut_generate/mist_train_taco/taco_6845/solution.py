"""
QUESTION:
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:


       All numbers will be positive integers.
       The solution set must not contain duplicate combinations.


Example 1:


Input: k = 3, n = 7
Output: [[1,2,4]]


Example 2:


Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

def find_combinations(k, n):
    def backtrack(to_return, temp, k, n, start):
        total = sum(temp)
        if total > n:
            return
        if len(temp) == k and total == n:
            to_return.append(temp[:])
            return
        for i in range(start, 10):
            temp.append(i)
            backtrack(to_return, temp, k, n, i + 1)
            temp.pop()
    
    to_return = []
    backtrack(to_return, [], k, n, 1)
    return to_return