"""
QUESTION:
Given a string 's'. The task is to find the smallest window length that contains all the characters of the given string at least one time.
For eg. A = aabcbcdbca, then the result would be 4 as of the smallest window will be dbca.
 
Example 1:
Input : "AABBBCBBAC"
Output : 3
Explanation : Sub-string -> "BAC"
Example 2:
Input : "aaab"
Output : 2
Explanation : Sub-string -> "ab"
 
Example 3:
Input : "GEEKSGEEKSFOR"
Output : 8
Explanation : Sub-string -> "GEEKSFOR"
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findSubString() which takes the string  S as input and returns the length of the smallest such window of the string.
Expected Time Complexity: O(256.N)
Expected Auxiliary Space: O(256)
 
Constraints:
1 ≤ |S| ≤ 10^{5}
String may contain both type of English Alphabets.
"""

def find_smallest_window_length(s: str) -> int:
    from collections import defaultdict
    
    # Dictionary to count occurrences of each character
    char_count = defaultdict(int)
    
    # Initialize the answer with infinity
    min_length = float('inf')
    
    # Initialize the start pointer
    start = 0
    
    # Count the number of unique characters in the string
    unique_chars = len(set(s))
    
    # Initialize the count of unique characters in the current window
    current_unique_count = 0
    
    # Iterate over the string with the end pointer
    for end in range(len(s)):
        # Increment the count of the current character
        char_count[s[end]] += 1
        
        # If this character is newly added to the window, increment the unique count
        if char_count[s[end]] == 1:
            current_unique_count += 1
        
        # If all unique characters are in the current window, try to minimize the window
        while current_unique_count == unique_chars:
            # Update the minimum length
            min_length = min(min_length, end - start + 1)
            
            # Decrement the count of the character at the start pointer
            char_count[s[start]] -= 1
            
            # If the count of the character at the start pointer becomes zero, decrement the unique count
            if char_count[s[start]] == 0:
                current_unique_count -= 1
            
            # Move the start pointer to the right
            start += 1
    
    return min_length