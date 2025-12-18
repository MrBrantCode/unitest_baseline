"""
QUESTION:
Given a string str, convert the first letter of each word in the string to uppercase. 
Example 1:
Input:
str = "i love programming"
Output: "I Love Programming"
Explanation:
'I', 'L', 'P' are the first letters of 
the three words.
Your Task:  
You dont need to read input or print anything. Complete the function transform() which takes s as input parameter and returns the transformed string.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N) to store resultant string  
Constraints:
1 <= N <= 10^{4}
The original string str only consists of lowercase alphabets and spaces to separate words.
"""

import string

def capitalize_words(s: str) -> str:
    """
    Converts the first letter of each word in the given string to uppercase.

    Parameters:
    s (str): The input string containing words to be capitalized.

    Returns:
    str: The transformed string with the first letter of each word capitalized.
    """
    return string.capwords(s)