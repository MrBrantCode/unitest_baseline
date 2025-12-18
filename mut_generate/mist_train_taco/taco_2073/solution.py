"""
QUESTION:
You are given a string $\mbox{S}$. 

$\mbox{S}$ contains alphanumeric characters only. 

Your task is to sort the string $\mbox{S}$ in the following manner:

All sorted lowercase letters are ahead of uppercase letters. 
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string $\mbox{S}$.

Constraints

$0<len(S)<1000$

Output Format

Output the sorted string $\mbox{S}$.

Sample Input
Sorting1234

Sample Output
ginortS1324
"""

def sort_string_special(S: str) -> str:
    def value_of_char(char: str) -> tuple:
        value = 0
        if char.isdigit():
            digit = int(char)
            value = (3, 2 if digit % 2 == 0 else 1)
        elif char.islower():
            value = (1,)
        elif char.isupper():
            value = (2,)
        return (value, char)
    
    return ''.join(sorted(S, key=value_of_char))