"""
QUESTION:
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.


Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"



Restrictions: 

 The string consists of lower English letters only.
 Length of the given string and k will in the range [1, 10000]
"""

def reverse_str_in_chunks(s: str, k: int) -> str:
    """
    Reverses the first k characters for every 2k characters in the string s.
    
    Parameters:
    - s (str): The input string consisting of lower English letters.
    - k (int): The integer specifying the chunk size.
    
    Returns:
    - str: The modified string after reversing the appropriate chunks.
    """
    for idx in range(0, len(s), 2 * k):
        s = s[:idx] + s[idx:idx + k][::-1] + s[idx + k:]
    return s