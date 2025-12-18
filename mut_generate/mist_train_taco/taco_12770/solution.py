"""
QUESTION:
Given a string consisting of lowercase english alphabets, reverse only the vowels present in it and print the resulting string.
Example 1:
Input:
S = "geeksforgeeks"
Output: geeksforgeeks
Explanation: The vowels are: e, e, o, e, e
Reverse of these is also e, e, o, e, e.
Example 2:
Input: 
S = "practice"
Output: prectica
Explanation: The vowels are a, i, e
Reverse of these is e, i, a.
 
Example 3:
Input: 
S = "bcdfg"
Output: bcdfg
Explanation: There are no vowels in S.
Your Task:
You don't need to read input or print anything. Your task is to complete the function modify() which takes the string S as input and returns the resultant string by reversing only the vowels present in S.
Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(|S|).
Constraints:
1<=|S|<=10^{5}
"""

def reverse_vowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s_list = list(s)
    vowel_positions = [i for i, char in enumerate(s) if char in vowels]
    vowel_chars = [s[i] for i in vowel_positions]
    
    # Reverse the list of vowel characters
    vowel_chars.reverse()
    
    # Replace the vowels in the original string with the reversed vowels
    for pos, char in zip(vowel_positions, vowel_chars):
        s_list[pos] = char
    
    return ''.join(s_list)