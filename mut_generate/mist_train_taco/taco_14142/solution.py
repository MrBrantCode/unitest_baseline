"""
QUESTION:
Given two positive numbers A and B. The task is to divide A by B and calculate the number of digits after decimal.
Example 1:
Input: A = 4, B = 5
Output: 1
Explaination: If 4 is divided by 5 the 
result is 0.8. So there is only 1 digit 
after decimal.
Example 2:
Input: A = 1, B = 3
Output: -1
Explaination: It's a recurring decimal when 
1 is divided by 3.
Your Task:
You do not need to read input or print anything. Your task is to complete the function countDecimal() which takes A and B as input parameters and returns the number of integers after the decimal point. It returns -1 if it is a recurring decimal.
Expected Time Complexity: O(B)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ A, B ≤ 10^{6}
"""

def count_decimal_digits(A: int, B: int) -> int:
    if A % B == 0:
        return 0
    
    result = str(A / B)
    
    if 'e-' in result:
        parts = result.split('e-')
        return int(parts[1])
    
    if '.' in result:
        parts = result.split('.')
        if len(parts[1]) >= 10:
            return -1
        return len(parts[1])
    
    return -1