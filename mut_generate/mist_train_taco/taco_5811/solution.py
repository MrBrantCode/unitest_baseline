"""
QUESTION:
Given a string S and an integer K. In one operation, you are allowed to choose any character of the string and change it to any other uppercase English character.You can perform this operation atmost K times.
Return the length of the longest substring containing same letter you can get after performing the above operations.
Note : S consists of only uppercase English letters.
Example 1:
Input : 
S = "ABBA"
K = 2
Output: 4
Explanation: Replace the 2 occurrences of 'A' with 2 'B's or vice-versa.
Example 2:
Input :
S = "AABAABB"
k = 2
Output: 6
Explanation: Replace the occurrence of 'B' with 'A' and form "AAAAAAB".
The substring "AAAAAA" has the most extended repeating letters, which is 6.
 
Your task :
You don't have to read input or print anything. Your task is to complete the function characterReplacement() which takes the string S and integer K as input and returns the longest substring containing same letter after performing specified operations.
 
Expected Time Complexity : (|S|)
Expected Auxiliary Space : O(1)
 
Constraints :
1 <= |S| <= 10^{5}
"""

def characterReplacement(S: str, K: int) -> int:
    i = 0
    j = 0
    char_dict = {}
    longest_substring = 0
    
    while j < len(S):
        char_dict[S[j]] = char_dict.get(S[j], 0) + 1
        
        while max(char_dict.values()) + K < j - i + 1:
            char_dict[S[i]] -= 1
            i += 1
        
        longest_substring = max(longest_substring, j - i + 1)
        j += 1
    
    return longest_substring