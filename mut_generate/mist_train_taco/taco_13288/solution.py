"""
QUESTION:
Given a string S, check whether it can be converted into the string "hello" by deleting some characters from it.
Note : S can have both uppercase and lowercase letters.
Example 1:
Input:
S = "bbbbbxxhhelllllooudd"
Output: 1
Explanation: The string hello is marked
in bold: bbbbbxxhhelllllooudd
Ã¢â¬â¹Example 2:
Input: 
S = "hlelo"
Output: 0
Explanation: It's impossible to convert
the given string into "hello".
Your Task:
You don't need to read input or print anything. Your task is to complete the function decode() which takes the string S as input and returns the true if the string can be converted to "hello", else return false.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=10^{5}
"""

def can_convert_to_hello(S: str) -> bool:
    target = 'hello'
    target_index = 0
    
    for char in S:
        if char == target[target_index]:
            target_index += 1
        if target_index == len(target):
            return True
    
    return False