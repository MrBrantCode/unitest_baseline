"""
QUESTION:
Given a binary string s and two integers x and y. Arrange the given string in such a way so that '0' comes X-times then '1' comes Y-times and so on until one of the '0' or '1' is finished. Then concatenate the rest of the string and find the final string.
Example 1:
Input:
X = 1, Y = 1, S = "0011"
Output: "0101"
Explanation: we put 1 '0' and 1 '1'
alternatively.
Example 2:
Input:
X = 1, Y = 1, S = "1011011"
Output: "0101111"
Explanation: We put '0' and '1' 
alternatively and in last we have to
put all '1' as there is no '0' left.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function arrangeString() which takes the string S and X, Y as inputs, and returns modified string.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ X, Y ≤ 10^{3}
1 ≤ |S| ≤ 10^{5}
"""

def arrange_string(s: str, x: int, y: int) -> str:
    zeros = s.count('0')
    ones = s.count('1')
    output = ''
    
    while ones > 0 and zeros > 0:
        output += '0' * min(x, zeros)
        zeros -= min(x, zeros)
        output += '1' * min(y, ones)
        ones -= min(y, ones)
    
    output += '0' * zeros
    output += '1' * ones
    
    return output