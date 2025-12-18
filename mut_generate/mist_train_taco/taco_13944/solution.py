"""
QUESTION:
Given a string S, you have to check if we can split it into four strings such that each string is non-empty and distinct from each other.
 
Example 1:
Input :
S = "geeksforgeeks"
Output:
1
Explanation:
"geeks", "for", "gee", "ks" are four
distinct strings that can form from
given string.
Example 2:
Input: 
S = "aaabb" 
Output:
0
Explanation:
It's not possible to split string S in four
distinct strings
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isPossible() which takes the string S as input parameter and returns 1 if it's possible to split S into four strings such that each string is non-empty and distinct from each other or return 0 otherwise. 
 
Expected Time Complexity: O(|S|^{3})
Expected Space Complexity: O(1)
Constraints:
1< |S| <=10000
"""

def can_split_into_four_distinct_strings(S: str) -> int:
    n = len(S)
    
    # If the length of the string is less than or equal to 3, it's not possible to split into four distinct strings
    if n <= 3:
        return 0
    
    # If the length of the string is 10 or more, it's always possible to split into four distinct strings
    if n >= 10:
        return 1
    
    # For strings with length between 4 and 9 (inclusive)
    st = set()
    for ch in S:
        st.add(ch)
    
    size = len(st)
    
    # If there are more than 3 unique characters, it's possible to split into four distinct strings
    if size > 3:
        return 1
    # If there are exactly 3 unique characters and the length of the string is at least 5, it's possible
    elif size == 3 and n >= 5:
        return 1
    # If there are exactly 2 unique characters and the length of the string is at least 7, it's possible
    elif size == 2 and n >= 7:
        return 1
    else:
        return 0