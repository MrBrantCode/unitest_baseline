"""
QUESTION:
Given a String S (in lowerCase only). Starting from letter 'a' which is the only source. for example:- "aaabcahd..." . Now you can only jump from one character to another in the form that a to b; b to c; c to d and so on. You have to find the maximum distance from source to destination. And if there is no place to jump on then print -1.
 
Example 1:
Input: aaabcb
Output: 6
Explanation: As 'a' will only jump to 'b' 
and the maximum distance will is 6.
Example 2:
Input: aabac
Output: 5
Explanation: As 'a' will only jump to 'b' 
and 'b' will jump to 'c' and distance 
is 5.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maximum_distance() which takes the string S as input parameter and returns the maximum distance. If not possible to reach at destination then return -1.
Expected Time complexity: O(n)
Expected Space complexity: O(n)
 
Constraints:
1 <= size of string <= 1000
"""

def maximum_distance(s: str) -> int:
    if 'a' not in s:
        return -1
    
    n = len(s)
    reversed_s = s[::-1]
    max_distance = -1
    current_index = s.index('a')
    
    for i in range(25):
        next_char = chr(i + 98)  # 'b' to 'z'
        temp_substring = s[current_index:]
        
        if next_char not in temp_substring:
            return max_distance
        
        max_distance = max(max_distance, n - reversed_s.index(next_char))
        current_index += temp_substring.index(next_char)
    
    return max_distance