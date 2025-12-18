"""
QUESTION:
Given two integer number n and d. The task is to find the number between 0 to n which contain the specific digit d.
Example 1 - 
Input
n = 20
d = 5
Output
5 15
Explanation:
For number till 20, 5 appears in 5 itself and 15.
Example 2 -
Input
n = 50
d = 2
Output
2 12 20 21 22 23 24 25 26 27 28 29 32 42
Explanation:
For number till 50, 2 appears in all these numbers.
Constraints:
0 <= n <= 103
0 <= d <= 9
Your Task :
You need to complete the function solve() that receives n and d as parameters and returns a vector containing answer.
Expected Time Complexity : O(n)
Expected Auxilliary Space : O(1)
"""

def find_numbers_with_digit(n: int, d: int) -> list:
    result = []
    d_str = str(d)
    
    for i in range(n + 1):
        if d_str in str(i):
            result.append(i)
    
    if not result:
        return [-1]
    
    return result