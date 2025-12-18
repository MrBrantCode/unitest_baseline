"""
QUESTION:
Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
Example 1:
Input:
s = V
Output: 5
Example 2:
Input:
s = III 
Output: 3
Your Task:
Complete the function romanToDecimal() which takes a string as input parameter and returns the equivalent decimal number. 
Expected Time Complexity: O(|S|), |S| = length of string S.
Expected Auxiliary Space: O(1)
Constraints:
1<=roman no range<=3999
"""

def roman_to_decimal(s: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_value = 0
    
    for i in range(len(s) - 1):
        if roman_values[s[i]] < roman_values[s[i + 1]]:
            decimal_value -= roman_values[s[i]]
        else:
            decimal_value += roman_values[s[i]]
    
    decimal_value += roman_values[s[-1]]
    return decimal_value