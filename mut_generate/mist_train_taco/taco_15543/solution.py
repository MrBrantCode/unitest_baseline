"""
QUESTION:
Given two numbers A and B which define a range, where A <= B. Find the count of total numbers in the given range [A … B] divisible by M.
Example 1:
Input: A = 6, B = 15, M = 3
Output: 4 
Explanation: 6, 9, 12, 15 are divisible
by 3.Hence answer is 4.
Example 2:
Input: A = 25, B = 100, M = 30
Output: 3
Explanation: 30, 60, 90 are divisible
by 30.Hence answer is 3.
Your Task:  
You dont need to read input or print anything. Complete the function countDivisibles() which takes n as input parameter and returns the count of total numbers in the given range [A … B] divisible by M.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= A, B, M <=10^{6}
"""

def count_divisibles(A: int, B: int, M: int) -> int:
    a = A // M
    b = B // M
    if A % M == 0:
        return b - a + 1
    return b - a