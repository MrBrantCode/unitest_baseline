"""
QUESTION:
Given four integers a, b, m, n . Find whether  pow(a,b) is greater than pow(m,n) or not. Where pow(x,y) denotes x raised to the power y. Output 1 if pow(a,b) is greater, output 0 if pow(m,n) is greater otherwise output -1 if both are equal. 
 
Example 1:
Input:
a = 2 , b = 2 , m = 3 , n = 2
Output:
0
Explanation:
2^{2} = 4, and 3^{2} = 9. 9>4. So,
the Output 0.
Example 2:
Input:
a = 1 , b = 23 , m = 1 , n = 989
Output:
-1
Explanation:
Both 1^{23} and 1^{989 }= 1. So,
the Output is -1. 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function greaterPower() which takes 4 Integers a,b,m and n as input and returns the answer.
 
Expected Time Complexity: O(max(log(a),log(m))
Expected Auxiliary Space: O(1)
 
Constraints:
0 <= b,n <= 10^{18}
1 <= a,m <= 10^{18}
"""

import math

def compare_powers(a, b, m, n):
    def log_power(x, y):
        if y == 0:
            return 1
        else:
            return y * math.log(x)
    
    log_a_b = log_power(a, b)
    log_m_n = log_power(m, n)
    
    if log_a_b > log_m_n:
        return 1
    elif log_a_b < log_m_n:
        return 0
    else:
        return -1