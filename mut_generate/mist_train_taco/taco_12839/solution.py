"""
QUESTION:
Check if the given string S is a Panagram or not. A pangram is a sentence containing every letter in the English Alphabet.
Example 1:
Input: S = "Pack mY box witH fIve dozen 
            liquor jugs"
Output: 1
Explanation: Given string contains all 
English Alphabets. 
Example 2:
Input: S = "geeksFORgeeks"
Output: 0
Explanation: Given string does not contain 
all English Alphabets. 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isPanagram() which takes the string as inputs and returns 1 if the given string is panagram, otherwise 0.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(constant)
Constraints:
1 ≤ |S| ≤ 10^{5}
"""

def is_panagram(s: str) -> int:
    # Convert the string to lowercase to handle case insensitivity
    s = s.lower()
    
    # Create a list of all alphabets
    alphabet = [chr(value) for value in range(ord('a'), ord('a') + 26)]
    
    # Check if each alphabet is present in the string
    for char in alphabet:
        if char not in s:
            return 0
    
    return 1