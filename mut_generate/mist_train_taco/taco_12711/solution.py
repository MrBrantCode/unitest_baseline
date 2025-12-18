"""
QUESTION:
Given an integer N represented in the form of a string, remove consecutive repeated digits from it.
Example 1:
Input:
N = 1224
Output: 124
Explanation: Two consecutive occurrences of 
2 have been reduced to one.
Ã¢â¬â¹Example 2:
Input: 
N = 1242
Output: 1242
Explanation: No digit is repeating 
consecutively in N.
Your Task:
You don't need to read input or print anything. Your task is to complete the function modify() which takes the integer N as input and returns the modified integer by removing all the consecutive duplicate occurrences in N.
Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(1).
Constraints:
1<=N<=10^{18}
"""

def remove_consecutive_duplicates(N: str) -> str:
    if not N:
        return N
    
    result = N[0]
    for i in range(1, len(N)):
        if N[i] != N[i - 1]:
            result += N[i]
    
    return result