"""
QUESTION:
You are simply given two numbers 355 and 113. You just have to find the value of 355/113 upto the decimal  k places . 
 
Example 1:
Input: k = 0
Output: 3
Explanation: 355/113 upto 0 decimal place is 3
Example 2:
Input: k = 1
Outptut: 3.1
Explanation: 355/113 upto 1 decimal place is 3.1
 
Your Task:
You don't need to read or print anything. Your task is to complete the function upto_K_places() which takes k as input parameter and returns 355/113 upto k decimal places in string format.
Expected Time Complexity: O(k)
Expected Space Complexity: O(1)
 
Constraints: 
1 <= k <= 10000
"""

def calculate_pi_upto_k_places(k: int) -> str:
    if k == 0:
        return "3"
    
    # Initial value of 355/113
    p = 355 % 113
    result = "3."
    
    # Multiply the remainder by 10 to start the division process
    p *= 10
    count = 0
    
    # Loop to calculate each decimal place
    while count != k:
        digit = p // 113
        result += str(digit)
        p = (p % 113) * 10
        count += 1
    
    return result