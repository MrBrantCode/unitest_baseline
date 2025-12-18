"""
QUESTION:
Given a string consisting of spaces,\t,\n and lower case  alphabets.Your task is to count the number of words where spaces,\t and \n work as separators.
 
Example 1:
Input: S = "abc def"
Output: 2
Explanation: There is a space at 4th
position which works as a seperator
between "abc" and "def"
 
Example 2:
Input: S = "a\nyo\n"
Output: 2
Explanation: There are two words "a"
and "yo" which are seperated by "\n".
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countWords() which accepts a string as input and returns number of words present in it.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
where N is length of given String.
Constraints:
2 <= Length of String <= 10^{6}
"""

def count_words(s: str) -> int:
    # Replace '\n' and '\t' with spaces
    s = s.replace('\\n', ' ').replace('\\t', ' ')
    
    # Initialize variables
    p = ''
    z = 0
    
    # Iterate through each character in the string
    for i in s:
        if i != ' ':
            p += i
        else:
            if len(p) > 0:
                z += 1
            p = ''
    
    # Check if there's a word left at the end
    if p != '':
        z += 1
    
    return z