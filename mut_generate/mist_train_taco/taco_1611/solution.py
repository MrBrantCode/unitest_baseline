"""
QUESTION:
Given three integers x, y, z, the task is to compute the value of GCD(LCM(x,y), LCM(x,z)) and return the value.
Where, GCD = Greatest Common Divisor, LCM = Least Common Multiple.
Example 1:
Input: x = 15, y = 20, z = 100
Output: 60
Explanation: GCD(LCM(15,20), LCM(15,100))
=GCD(60,300)=60.
Ã¢â¬â¹Example 2:
Input: x = 30, y = 40, z = 400
Output: 120
Explanation: GCD(LCM(30,40), LCM(30,400))
=GCD(120,1200)=120.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findValue() which takes x, y, z as inputs and returns the answer.
Expected Time Complexity: O(max(log x, log y, log z))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ x, y, z ≤ 10^{6}
"""

def compute_gcd_of_lcms(x: int, y: int, z: int) -> int:
    def gcd(a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    lcm1 = int(x * y / gcd(x, y))
    lcm2 = int(x * z / gcd(x, z))
    return gcd(lcm1, lcm2)