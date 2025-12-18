"""
QUESTION:
Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet (either lowercase or uppercase or both). For example, we say the letter A is present in the string if either 'a' is present or 'A' is present.
Example 1:
Input:
S = Bawds jog, flick quartz, vex nymph
Output: 1
Explanation: In the given input, there
are all the letters of the English
alphabet. Hence, the output is 1.
Example 2:
Input:
S = sdfs
Output: 0
Explanation: In the given input, there
aren't all the letters present in the
English alphabet. Hence, the output
is 0.
Your Task:
 You need to complete the function checkPangram() that takes a string as a parameter and returns true if the string is a pangram, or else it returns false.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(Number of distinct characters).
Constraints:
1 ≤ |S| ≤ 10^{4}
"""

def is_pangram(s: str) -> bool:
    # Convert the string to lowercase to handle case insensitivity
    s = s.lower()
    
    # Create a set of characters from the string
    char_set = set(s)
    
    # Filter out only the alphabetic characters
    alphabets = {char for char in char_set if 'a' <= char <= 'z'}
    
    # Check if the set of alphabetic characters contains all 26 letters
    return len(alphabets) == 26