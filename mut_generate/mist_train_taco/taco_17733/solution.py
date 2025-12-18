"""
QUESTION:
Given an integer N, print all the N digit numbers in increasing order, such that their digits are in strictly increasing order(from left to right).
Example 1:
Input:
N = 1
Output:
0 1 2 3 4 5 6 7 8 9
Explanation:
Single digit numbers are considered to be 
strictly increasing order.
Example 2:
Input:
N = 2
Output:
12 13 14 15 16 17 18 19 23....79 89
Explanation:
For N = 2, the correct sequence is
12 13 14 15 16 17 18 19 23 and so on 
up to 89.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function increasingNumbers() which takes an integer N as an input parameter and return the list of numbers such that their digits are in strictly increasing order.
Expected Time Complexity: O(9^{N})
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 9
"""

def generate_increasing_numbers(N):
    def solve(k, n, curr, prev=0):
        if k == n:
            result.append(curr)
            return
        for i in range(prev + 1, 10):
            curr = curr * 10 + i
            solve(k + 1, n, curr, i)
            curr = curr // 10

    result = [] if N != 1 else [0]
    solve(0, N, 0)
    return result