"""
QUESTION:
Given two numbers as strings s1 and s2. Calculate their Product.
Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers.
Example 1:
Input:
s1 = "33"
s2 = "2"
Output:
66
Example 2:
Input:
s1 = "11"
s2 = "23"
Output:
253
Your Task: You don't need to read input or print anything. Your task is to complete the function multiplyStrings() which takes two strings s1 and s2 as input and returns their product as a string.
Expected Time Complexity: O(n_{1}* n_{2})
Expected Auxiliary Space: O(n_{1 }+ n_{2}); where n_{1} and n_{2} are sizes of strings s1 and s2 respectively.
Constraints:
1 ≤ length of s1 and s2 ≤ 10^{3}
"""

def multiply_strings(s1: str, s2: str) -> str:
    # Determine the sign of the result
    sign = 1
    if s1[0] == '-':
        sign *= -1
        s1 = s1[1:]
    if s2[0] == '-':
        sign *= -1
        s2 = s2[1:]
    
    # Initialize result array with zeros
    result = [0] * (len(s1) + len(s2))
    
    # Reverse the strings to facilitate multiplication
    s1 = s1[::-1]
    s2 = s2[::-1]
    
    # Perform multiplication digit by digit
    for i in range(len(s1)):
        for j in range(len(s2)):
            result[i + j] += (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10
    
    # Remove leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    # Convert result array to string
    result = result[::-1]
    result_str = ''.join(map(str, result))
    
    # Add sign if necessary
    if sign == -1:
        result_str = '-' + result_str
    
    return result_str