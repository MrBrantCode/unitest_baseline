"""
QUESTION:
Geek played three matches and he wants to represent his scores as an array and in the Concatenated string form.
Example 1:
Input:
2 7 5
Output:
[ 2,7,5 ]
275
Your Task:
This is a function problem. You only need to complete the function arrayForm() and stringForm() that takes three integers a,b,c as parameters and that return array form and string form respectively. Don't print newline, it will be added by the driver code.
Constraint:
1<=a,b,c<=10
"""

def convert_scores(a, b, c):
    array_form = [a, b, c]
    string_form = str(a) + str(b) + str(c)
    return array_form, string_form