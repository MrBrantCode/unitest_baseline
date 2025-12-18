"""
QUESTION:
Given a string S, containing special characters and all the alphabets, reverse the string without
affecting the positions of the special characters.
Example 1:
Input: S = "A&B"
Output: "B&A"
Explanation: As we ignore '&' and
then reverse, so answer is "B&A".
Example 2:
Input: S = "A&x#
Output: "x&A#"
Explanation: we swap only A and x.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function reverse() which takes the string as inputs and returns required reverse string.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)
Constraints:
1 ≤ |S| ≤ 10^{5}
"""

def reverse_string_without_special_chars(s: str) -> str:
    i = 0
    j = len(s) - 1
    s = list(s)
    
    while i < j:
        if s[i].isalpha():
            if s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                j -= 1
        else:
            i += 1
    
    return ''.join(s)