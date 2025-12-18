"""
QUESTION:
Given two positive integers num1 and num2, the task is to find the sum of the two numbers on a 12 hour clock rather than a number line.
Example 1:
Input: num1 = 5, num2 = 7
Output: 0
Explaination: 5+7=12, which in 12 hour 
clock format is 0.
Example 2:
Input: num1 = 3, num2 = 5
Output: 8
Explaination: 3+5=8, which is 12 hour 
format is intact.
Your Task:
You do not need to read input or print anythign. Your task is to complete the function clockSum() which takes num1 and num2 as input parameters and returns the 12 hour clock format addition of the numbers.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ num1, num2 ≤ 50
"""

def clock_sum(num1: int, num2: int) -> int:
    s = num1 + num2
    if s == 12:
        return 0
    elif s < 12:
        return s
    else:
        return s % 12