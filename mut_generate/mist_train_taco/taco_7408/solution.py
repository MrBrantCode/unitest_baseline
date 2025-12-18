"""
QUESTION:
Given a string S without spaces, a character ch, and an integer count, the task is to find the string after the specified character has occurred count number of times. 
Example 1:
Input:  S = "Thisisdemostring", ch = 'i', 
count = 3
Output: ng
Explanation: Substring of S after the 3rd
occurrence of 'i' is "ng"
Example 2:
Input:  S = "Thisisdemostri", ch = 'i', 
count = 3
Output: Empty string
Explanation: 'i' occurce 3rd time at 
last index
Your Task:
Your task is to complete the function printString() which takes a single, a character, and a count as inputs and returns the string. You need not take any input or print anything.
Note:  “Empty string” should be returned incase of any unsatisfying conditions (Given character is not present, or present but less than given count, or given count completes on the last index). If given count is 0, then given character doesn’t matter, just return the whole string.
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(1)
Constraints:
1 <= |S| <= 10^{5}
Assume upper case and lower case
alphabets as different
"""

def find_substring_after_char(S: str, ch: str, count: int) -> str:
    if count == 0:
        return S
    
    occurrences = [match.start() for match in re.finditer(re.escape(ch), S)]
    
    if len(occurrences) >= count:
        index = occurrences[count - 1] + 1
        if index >= len(S):
            return 'Empty string'
        return S[index:]
    else:
        return 'Empty string'