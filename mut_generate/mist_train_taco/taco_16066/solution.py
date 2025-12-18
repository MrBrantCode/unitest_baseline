"""
QUESTION:
Given an string of binary number n. The task is to convert binary fractional n into its decimal equivalent.
 
Example 1:
Input:
n = 110.101
Output:
6.625
Explanation:
The given binary String is equivalent
to (6.625)_{10}
Example 2:
Input:
n = 101.1101
Output:
5.8125
Explanation:
The given binary String is equivalent
to (5.8125)_{10}
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function convertToDecimal() which takes an String n as input and returns the answer.
 
Expected Time Complexity: O(|n|)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= |n| <= 50
"""

def binary_fractional_to_decimal(n: str) -> float:
    # Split the input string into integer and fractional parts
    l = n.split('.')
    
    # Convert the integer part to decimal
    integer_part = l[0]
    d = len(integer_part) - 1
    c = 0
    for i in integer_part:
        if i == '1':
            c += 2 ** d
        d -= 1
    
    # Convert the fractional part to decimal
    fractional_part = l[1] if len(l) > 1 else ''
    e = 0.5
    h = 0
    for i in fractional_part:
        if i == '1':
            h += e
        e /= 2
    
    # Combine the integer and fractional parts
    return c + h