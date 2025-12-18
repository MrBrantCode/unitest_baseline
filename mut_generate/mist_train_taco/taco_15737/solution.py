"""
QUESTION:
Given a string s and an integer k, the task is to reduce the string by applying the following operation:
Choose a group of k consecutive identical characters and remove them.
The operation can be performed any number of times until it is no longer possible.
Example 1:
Input:
k = 2
s = "geeksforgeeks"
Output:
gksforgks
Explanation:
Modified String after each step: 
"geeksforgeeks" -> "gksforgks"
Example 2:
Input:
k = 2
s = "geegsforgeeeks" 
Output:
sforgeks
Explanation:
Modified String after each step:
"geegsforgeeeks" -> "ggsforgeks" -> "sforgeks"
Your Task:  
You don't need to read input or print anything. Complete the function Reduced_String() which takes integer k and string s as input parameters and returns the reduced string.
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)
Constraints:
1 ≤ |s| ≤ 10^{5}
1 ≤ k ≤ |s|
"""

def reduce_string(k: int, s: str) -> str:
    if k == 1:
        return ''
    
    stack = ['A']  # Initialize stack with a dummy character to avoid empty stack issues
    count = 1
    
    for char in s:
        if stack[-1] != char:
            stack.append(char)
            count = 1
        else:
            count += 1
            if count == k:
                while count > 1:
                    stack.pop()
                    count -= 1
            else:
                stack.append(char)
    
    return ''.join(stack)[1:]  # Remove the dummy character from the result