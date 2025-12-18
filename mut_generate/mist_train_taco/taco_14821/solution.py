"""
QUESTION:
Given a String(only lower case letters) , check if any substring has occured Twice :

 Example : iwsagoodboody
Here, substring  "ood" occurs twice.

Output "YES"  if there is any such substring else output "NO" .(without qoutes)

Input:

First line of input consists of an integer T (1 ≤ T ≤ 100) ,  indicating the number of test cases. 
For each test case, there will be a string s (1 ≤ |s| ≤ 2000)

Output:
    Print "YES"  if there is any such substring else Print "NO" .(without quotes)

SAMPLE INPUT
3
abcdefghi
dogsbarkatdogs
howtheydo

SAMPLE OUTPUT
NO
YES
YES
"""

def has_repeated_substring(s: str) -> str:
    """
    Check if any substring of the given string occurs twice.

    Parameters:
    s (str): The input string to check for repeated substrings.

    Returns:
    str: "YES" if any substring occurs twice, otherwise "NO".
    """
    for i in range(1, len(s)):
        seen = set()
        for j in range(len(s) - i + 1):
            sub = s[j:j+i]
            if sub in seen:
                return "YES"
            seen.add(sub)
    return "NO"