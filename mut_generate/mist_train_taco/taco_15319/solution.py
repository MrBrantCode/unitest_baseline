"""
QUESTION:
Given a number N in the form of string, your task is to find the remainder when the number is divided by 7.
Note: The given number is very large and so the Input is taken as a String.
 
Example 1:
Input:
N = "98"
Output:
0
Explanation:
98 when divided by 7 gives a
remainder of 0.
Example 2:
Input:
N = "13"
Output:
6
Explanation:
13 when divided by 7 gives a
remainder of 6.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findRemainder() which takes a String N as input and returns the answer.
 
Expected Time Complexity: O(|N|)
Expected Auxiliary Space: O(|N|)
 
Constraints:
0 <= |N| <= 10^{3}
"""

def find_remainder(N: str) -> int:
    return int(N) % 7