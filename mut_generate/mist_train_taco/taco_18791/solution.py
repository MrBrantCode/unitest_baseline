"""
QUESTION:
Given a string S consisting of upper/lower-case alphabets and empty space characters ‘ ‘. The string may contain spaces at the end. You will have return the length of last word which consists of alphabets only.
Example 1:
Input:
S = "Geeks for Geeks"
Output: 5
Explanation: The last word is "Geeks" 
             of length 5.
Example 2:
Input:
S = "Start Coding Here "
Output: 4
Explanation: The last word is "Here" of
             length 4.
Your Task:
You don't need to read input or print anything.Your task is to complete the function findLength() which takes a single argument(string S) and returns the length of last word of the string.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1<=|S|<=100
|S| denotes the length of the string S.
"""

def find_length_of_last_word(s: str) -> int:
    n = len(s)
    count = 0
    for i in range(n - 1, -1, -1):
        if s[i] == ' ' and count > 0:
            return count
        elif s[i] != ' ':
            count += 1
    return count