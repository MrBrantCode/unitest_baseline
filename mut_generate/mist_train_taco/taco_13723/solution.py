"""
QUESTION:
Given a binary string S of 0 and 1, check if the given string is valid or not. The given string is valid when there is no zero is present in between 1s.
Example 1:
Input:
S = "100"
Output: VALID
Explanation: 100. The string have just a
single 1, hence it is valid.
Example 2:
Input: 
S = "1110001"
Output: INVALID
Explanation: 1110001. There are 3 zeros
between the 3rd and the 4th ones. Hence,
it's an invalid string.
Your Task:
You don't need to read input or print anything, Your task is to complete the function checkBinary() which takes a binary string as input are returns true if the string is valid. Else, it returns false.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=length(S)<=10^{5 }
"""

def is_valid_binary_string(s: str) -> bool:
    one_found = False
    zero_found_after_one = False
    
    for char in s:
        if char == '1':
            if zero_found_after_one:
                return False
            one_found = True
        elif char == '0':
            if one_found:
                zero_found_after_one = True
    
    return True