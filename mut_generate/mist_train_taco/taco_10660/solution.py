"""
QUESTION:
If all decimal numbers are concatenated in a string then we will get a string which looks like string P as shown below. We need to tell Nth character of this string.
P = “12345678910111213141516171819202122232425262728293031….”
Example 1:
Input: N = 10
Output: 1
Explaination: From the given portion of the 
string you can see that the 10th character is 
'1'.
Example 1:
Input: N = 11
Output: 10
Explaination: From the given portion of the 
string yuou can see that the 11th character is 
'0'.
Your Task:
You do not need to read input or print anything. Your task is to complete the function NthCharacter() which takes N as input parameter and returns the Nth character of the string P.
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
"""

def NthCharacter(N):
    s = ''
    for i in range(1, N + 1):
        s += str(i)
    return s[N - 1]