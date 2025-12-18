"""
QUESTION:
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

Input Format
The first and only line of input contains the String S  

Output Format
Print the resultant String on a single line.   

Constraints
 1 ≤ |S| ≤ 100   where |S|  denotes the length of string S.  

SAMPLE INPUT
abcdE

SAMPLE OUTPUT
ABCDe
"""

def toggle_case(S: str) -> str:
    """
    Converts all uppercase letters in the input string to lowercase and all lowercase letters to uppercase.

    Parameters:
    S (str): The input string containing uppercase and lowercase English alphabets.

    Returns:
    str: The resultant string with toggled cases.
    """
    if not (1 <= len(S) <= 100):
        raise ValueError("The length of the string must be between 1 and 100 inclusive.")
    
    new_list = []
    for el in S:
        if el.islower():
            new_list.append(el.upper())
        else:
            new_list.append(el.lower())
    
    return ''.join(new_list)