"""
QUESTION:
Given a fraction. Convert it into a decimal. 
If the fractional part is repeating, enclose the repeating part in parentheses.
 
Example 1:
Input: numerator = 1, denominator = 3
Output: "0.(3)"
Explanation: 1/3 = 0.3333... So here 3 is 
recurring.
Example 2:
Input: numerator = 5, denominator = 2
Output: "2.5"
Explanation: 5/2 = 2.5
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function fractionToDecimal() which takes numerator and denominator as input parameter and returns its decimal form in string format.
Note: In case, the numerator is divisible by the denominator, just print the integer value.
 
Expected Time Compelxity: O(k) where k is constant.
Expected Space Complexity: O(k)
 
Constraints:
1 ≤ numerator, denominator ≤ 2000
"""

def fraction_to_decimal(numerator: int, denominator: int) -> str:
    quotient = numerator // denominator
    remainder = numerator % denominator
    result = str(quotient)
    
    if remainder == 0:
        return result
    
    result += '.'
    mp = {}
    
    while remainder != 0:
        if remainder in mp:
            pos = mp[remainder]
            result = result[:pos] + '(' + result[pos:] + ')'
            break
        else:
            mp[remainder] = len(result)
            remainder *= 10
            quotient = remainder // denominator
            remainder = remainder % denominator
            result += str(quotient)
    
    return result