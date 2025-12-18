"""
QUESTION:
Given an odd number in the form of string, the task is to make largest even number possible from the given number provided one is allowed to do only one swap operation, if no such number is possible then return the input string itself.
Example 1:
Input:
s = 4543
Output: 4534
Explanation: Swap 4(3rd pos) and 3.
 
Example 2:
Input:
s = 1539
Output: 1539
Explanation: No even no. present.
 
Your Task:  
You dont need to read input or print anything. Complete the function makeEven() which takes a string s as input parameter and returns a string after performing given operations.
 
Expected Time Complexity: O(Length of Input string).
Expected Auxiliary Space: O(1).
 
Constraints:
1 <= Length of odd number string<= 10^{5}
"""

def make_largest_even_number(s: str) -> str:
    s = list(s)
    for i in range(len(s)):
        if int(s[i]) < int(s[-1]) and int(s[i]) % 2 == 0:
            (s[i], s[-1]) = (s[-1], s[i])
            return ''.join(s)
    for i in range(1, len(s) + 1):
        if int(s[-i]) > int(s[-1]) and int(s[-i]) % 2 == 0:
            (s[-i], s[-1]) = (s[-1], s[-i])
            return ''.join(s)
    return ''.join(s)