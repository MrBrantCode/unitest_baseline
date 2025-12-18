"""
QUESTION:
A function f is defined as follows F(N)= (1) +(2*3) + (4*5*6) ... N. Given an integer N the task is to print the F(N)th term.
Example 1:
Input: N = 5
Output: 365527
Explaination: F(5) = 1 + 2*3 + 4*5*6 + 7*8*9*10 
+ 11*12*13*14*15 = 365527.
Your Task:
You do not need to readd input or print anything. Your task is to complete the function sequence() which takes N as input parameter and returns the value of F(N).
Expected Tiime Complexity: O(N^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10
"""

def calculate_sequence(N: int) -> int:
    ans = 0

    def recursion(digits, count):
        if digits > N:
            return
        temp = 1
        for i in range(digits):
            temp *= count
            count += 1
        nonlocal ans
        ans += temp
        recursion(digits + 1, count)

    recursion(1, 1)
    return ans