"""
QUESTION:
Given a number in form of a string s. The task is to find whether the number is valid indian mobile number or not.
Rules for valid :-indian mobile number
	The number should contain 10 or 11 or 12 digits.
	If it contains 10 digits, then first  digit should be 7 or 8 or 9.
	If it contains 11 digits, then first  digit should be 0 and second rule follwed.
	If it contains 12 digits, then first two digits should be 91 and second rule followed 
Example 1:
Input: s = "912345678999"
Output: 0
Example 2:
Input: s = "123456789"
Output: 0
 
Your Task:
You don't need to read or print anything. Your task is to complete the function is_valid() which takes s as input parameter and returns 1 if it is valid indian mobile number otherwise returns 0.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
Constraints:
1 <= |s| <= 13
"""

import re

def is_valid_indian_mobile_number(s: str) -> int:
    if len(s) >= 10 and len(s) <= 12:
        if len(s) == 10:
            ans = re.search('^[7-9]', s)
            if ans:
                return 1
            else:
                return 0
        if len(s) == 11:
            ans = re.search('^0[7-9]', s)
            if ans:
                return 1
            else:
                return 0
        if len(s) == 12:
            ans = re.search('^91[7-9]', s)
            if ans:
                return 1
            else:
                return 0
    else:
        return 0