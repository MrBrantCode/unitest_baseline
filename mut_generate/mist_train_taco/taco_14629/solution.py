"""
QUESTION:
Given a string str and an integer K, find whether the string can be changed into a pangram after at most k operations. A pangram is a sentence containing every letter in the english alphabet. A single operation can be used to swap an existing alphabetic character with any other alphabetic character.
Example 1:
Input:
str = "the quick brown fox jumps over the lazy dog"
k = 0
Output: 1
Explanation: the sentence contains all 26 characters 
and is already a pangram. 
Example 2:
Input:
str = "aaaaaaaaaaaaaaaaaaaaaaaaaa"
k = 25
Output: 1
Explanation: The word contains 26 instances of 'a'.
Since only 25 operations are allowed. We can keep
1 instance and change all others to make str a pangram.
Your Task:  
You dont need to read input or print anything. Complete the function kPangram() which takes str and k as input parameters and returns a boolean value which denotes if pangram is possible or not.
Expected Time Complexity: O(N) where N is length of str.
Expected Auxiliary Space: O(1)  
Constraints:
1<= N <= 10^{4}
String may contain duplicate characters.
String can contain only lowercase alphabets or space.
"""

def is_pangram_possible(string: str, k: int) -> bool:
    # Set to store unique alphabetic characters in the string
    unique_chars = set()
    
    # Count of alphabetic characters in the string
    char_count = 0
    
    # Iterate through each character in the string
    for char in string:
        if 'a' <= char <= 'z':
            unique_chars.add(char)
            char_count += 1
    
    # Check if the string can be converted to a pangram with at most k operations
    if char_count >= 26 and 26 - len(unique_chars) <= k:
        return True
    
    return False