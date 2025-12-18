"""
QUESTION:
Given three  integers N, x and y, a number A is formed by repeating N x times and another number B is formed by repeating N y times. You need to find the GCD(A,B). 
 
Example 1:
Input: N = 1, x = 1, y = 1
Output: 1
Explanation: A = 1, B = 1, GCD(1, 1)  = 1
Example 2:
Input: N = 2, x = 2, y = 2
Output: 2
Explanation: A = 22, B = 222, GCD(22, 222) = 2
 
Your Task:
You don't need to read or print anything. Your task is to complete the function FindGcd() which takes N, x and y as input parameter and returns GCD(A, B) in string form.
 
Expected Time Complexity: O(Log_{10}(N) * GCD(x, y))
Expected Space Complexity: O(Log_{10}(N) * GCD(x, y))
 
Constraints:
1 <= x, y <= 100000
1 <= N <= 10^{18}
"""

def find_gcd(N: int, x: int, y: int) -> str:
    # Helper function to form the number by repeating N x times
    def form_number(n: int, times: int) -> int:
        return int(str(n) * times)
    
    # Helper function to compute the GCD of two numbers
    def gcd(a: int, b: int) -> int:
        return a if b == 0 else gcd(b, a % b)
    
    # Calculate the GCD of x and y
    gcd_xy = gcd(x, y)
    
    # Form the number by repeating N gcd_xy times
    result = form_number(N, gcd_xy)
    
    # Return the result as a string
    return str(result)