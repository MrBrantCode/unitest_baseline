"""
QUESTION:
Given an integer n, the task is to find whether n can be written as sum of three consecutive integer.
Example 1:
Input: n = 6
Output: 1 2 3 
Explanation: 6 = 1+2+3
Hence 6 can be written as sum of 
three consecutive integer.
Example 2:
Input: n = 7
Output: -1
Explanation: 7 cannot be written as 
sum of three consecutive integer.
Your Task:  
You dont need to read input or print anything. Complete the function consecutiveSum() which takes n as input parameter and returns a vector contains of three consecutive integers if it is possible else -1.
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1<= n <=10000
"""

def find_consecutive_sum(n: int) -> list:
    if n % 3 != 0:
        return [-1]
    a = n // 3
    return [a - 1, a, a + 1]