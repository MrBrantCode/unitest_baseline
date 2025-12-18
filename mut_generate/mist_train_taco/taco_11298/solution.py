"""
QUESTION:
Given a floating point number in string format s, check whether it is even or odd.
 
Example 1:
Input: 
n = 4
s = 97.8
Output: EVEN
Explanation: 8 is even number.
Example 2: 
Input:
n = 6
s = 100.70
Output: ODD
Explanation: Trailing 0s after dot do not matter.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isEven() which accepts a string s(floating point number) and the integer n(denotes the length of the string s) as input parameter and returns a boolean value.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= n <= 10^{5}
n is the length of the string s.^{ }
"""

def is_even(s: str, n: int) -> bool:
    # Split the string at the decimal point
    parts = s.split('.')
    
    # Get the fractional part
    fractional_part = parts[1]
    
    # Remove trailing zeros from the fractional part
    fractional_part = fractional_part.rstrip('0')
    
    # If the fractional part is empty, check the integer part
    if not fractional_part:
        return int(parts[0]) % 2 == 0
    
    # Convert the fractional part to an integer and check its parity
    return int(fractional_part) % 2 == 0