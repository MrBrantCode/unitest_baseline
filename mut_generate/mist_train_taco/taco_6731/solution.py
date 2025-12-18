"""
QUESTION:
Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given a number, the task is to check if it is a Strong Number or not.
 
Example 1:
Input: 145
Output: 1
Explanation: 1! + 4! + 5! = 145
Example 2:
Input: 5314
Output: 0
Explanation: 5! + 3! + 1! + 4! 
is not equal to 5314.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function is_StrongNumber() which takes the number as input parameter and returns 1 if it is Strong Number otherwise returns 0.
 
Expected Time Complexity : O(Number of digits in N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 10000
"""

def is_strong_number(n: int) -> int:
    def fact(x: int) -> int:
        if x == 1 or x == 0:
            return 1
        return x * fact(x - 1)
    
    sumo = 0
    m = n
    while n != 0:
        r = n % 10
        n = n // 10
        sumo = sumo + fact(r)
    
    if sumo == m:
        return 1
    else:
        return 0