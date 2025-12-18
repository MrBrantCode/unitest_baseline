"""
QUESTION:
Given a binary string S. The task is to count the number of substrings that starts and end with 1.
Note: The starting and the ending 1s should be different.
Example 1:
Input:
S = "10101"
Output: 3
Explanation: The 3 substrings are "101",
"10101" and "101".
Ã¢â¬â¹Example 2:
Input: 
S = "100"
Output: 0
Explanation: No substring that starts and
ends with 1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countSubstr() which takes the string S as input and returns the count of the substrings that start and end with 1.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).
Constraints:
1 <= |S| <= 1000
"""

def count_substrings_with_different_ones(s: str) -> int:
    sum_count = 0
    count_ones = 0
    
    for char in s:
        if char == '1':
            sum_count += count_ones
            count_ones += 1
    
    return sum_count