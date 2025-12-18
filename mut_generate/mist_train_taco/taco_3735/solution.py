"""
QUESTION:
Given two integer numbers a and b, the task is to find count of all common divisors of given numbers.
Example 1:
Input: a = 12, b = 24
Output: 6 
Explanation: all common divisors 
are 1, 2, 3, 4, 6 and 12.
Example 2:
Input: a = 3, b = 17
Output: 1
Explanation: all common divisors are 1.
Your Task:  
You dont need to read input or print anything. Complete the function commDiv() which takes n as input parameter and returns the number of common divisors.
Expected Time Complexity: O(sqrt(n))
Expected Auxiliary Space: O(1)
Constraints:
1<= a,b <=1000
"""

def count_common_divisors(a: int, b: int) -> int:
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    gcd_value = gcd(a, b)
    count = 0
    
    for i in range(1, int(gcd_value**0.5) + 1):
        if gcd_value % i == 0:
            count += 1
            if i != gcd_value // i:
                count += 1
    
    return count