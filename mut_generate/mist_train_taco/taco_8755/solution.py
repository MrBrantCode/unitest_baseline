"""
QUESTION:
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:


Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"


Note:


       If there is no such window in S that covers all characters in T, return the empty string "".
       If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

def find_min_window(s: str, t: str) -> str:
    left = -1
    right = 0
    result = ''
    total_match = 0
    d = {}
    
    # Initialize the dictionary with the count of each character in t
    for c in t:
        d[c] = d.get(c, 0) + 1
    
    # Iterate over the string s
    for right in range(len(s)):
        c = s[right]
        d[c] = d.get(c, 0) - 1
        
        # If the character is part of t and we have matched the required count
        if d[c] >= 0:
            total_match += 1
            
            # If we have matched all characters in t
            if total_match == len(t):
                total_match -= 1
                left += 1
                
                # Move the left pointer to the right to find the minimum window
                while d[s[left]] < 0:
                    d[s[left]] += 1
                    left += 1
                
                d[s[left]] += 1
                
                # Update the result if the current window is smaller
                if result == '' or len(result) > right - left:
                    result = s[left:right + 1]
    
    return result