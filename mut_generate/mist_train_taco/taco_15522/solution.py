"""
QUESTION:
Given two numbers A and B, the task is to find f(A^{B}). f(n) which takes a positive integer n as input and does the following:
f(n):
if n < 10  
    return n
else return f( sum_of_digits(n) )
 
Example 1:
Input: A = 6, B = 6
Output: 9
Explanation: 
f(6^{6}) = f(46656) = f(27) = f(9) = 9
Example 2:
Input: A = 7, B = 3
Output: 1
Explanation: 
f(7^{3}) = f(343) = f(10) = f(1) = 1
 
Your Task:
You don't need to read or print anything. Your task is to complete the function SumofDigits() which takes A and B as input parameters and returns f(A^{B}).
 
Expected Time Complexity: O(Log(B))
Expected Space Complexity: O(1)
 
Constraints:
1 <= A, B <= 10^{9}
"""

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def f(n):
    while n >= 10:
        n = sum_of_digits(n)
    return n

def calculate_f_of_power(A, B):
    k = 1
    while B:
        if B & 1:
            k = k * A % 9
        A = A * A % 9
        B = B >> 1
    if k == 0:
        return 9
    return k