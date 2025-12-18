"""
QUESTION:
Create a function `shortest_palindrome(s)` that takes a string `s` as input and returns the shortest palindrome that can be obtained by adding characters to the end of `s`. The function should not modify the original string. 

The function should work as follows: if `s` is already a palindrome, it should return `s` as is. If `s` is not a palindrome, it should find the longest prefix of `s` that is also a suffix of the reversed `s`, and then add the remaining characters of `s` (in reverse order) to the end of the prefix. 

Additionally, write a main function `program()` that takes a string input from the user, checks whether it is a palindrome or not, and if it is not, asks the user whether they want to convert it to a palindrome. If the user agrees, it should call the `shortest_palindrome(s)` function and print the result.
"""

def shortest_palindrome(s):
    """
    This function takes a string `s` as input and returns the shortest palindrome that can be obtained by adding characters to the end of `s`.
    
    Parameters:
    s (str): The input string
    
    Returns:
    str: The shortest palindrome that can be obtained by adding characters to the end of `s`
    """
    i = 0
    for j in range(len(s)-1, -1, -1):
        if s[i] == s[j]:
            i += 1
    if i == len(s):
        return s
    else:
        return s[:i-1:-1] + shortest_palindrome(s[0:i]) + s[i:]