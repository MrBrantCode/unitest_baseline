"""
QUESTION:
Given a string s, extract all the integers from s. 
Example 1:
Input:
s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 
     3: Rishabh Gupta56"
Output: 1 2 3 56
Explanation: 
1, 2, 3, 56 are the integers present in s.
Example 2:
Input:
s = "geeksforgeeks"
Output: No Integers
Explanation: 
No integers present in the string.
 
Your Task:
You don't need to read input or print anything. Complete the function extractIntegerWords() which takes string s as input and returns a list of integers. If an empty list is returned the output is printed as "No Integers".
 
Expected Time Complexity: O(|s|).
Expected Auxiliary Space: O(|s|).
 
Constraints:
1<=|s|<=10^{5}
"""

def extract_integers(s: str) -> list[int]:
    """
    Extracts all integers from the given string `s`.

    Parameters:
    s (str): The input string from which integers are to be extracted.

    Returns:
    list[int]: A list of integers found in the string. If no integers are found, the list will be empty.
    """
    res = []
    current_number = ''
    
    for char in s:
        if char.isdigit():
            current_number += char
        elif current_number:
            res.append(int(current_number))
            current_number = ''
    
    if current_number:
        res.append(int(current_number))
    
    return res