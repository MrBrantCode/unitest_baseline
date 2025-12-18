"""
QUESTION:
You are given a string S, convert it into a magical string.
A string can be made into a magical string if the alphabets are swapped in the given manner: a->z or z->a, b->y or y->b, and so on.  
 
Note: All the alphabets in the string are in lowercase.
 
Example 1:
Input:
S = varun
Output:
ezifm
Explanation:
Magical string of "varun" 
will be "ezifm" 
since v->e , a->z , 
r->i , u->f and n->m.
 
Example 2:
Input:
S = akshay
Output:
zphszb
Explanation:
Magical string of "akshay" 
will be "zphszb" 
since a->z , k->p , s->h , 
h->s , a->z and y->b.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function magicalString() which takes the string S and returns the magical string.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
 
Constraints:
1<=Length of String<=100
"""

def convert_to_magical_string(S: str) -> str:
    """
    Converts a given string into its magical form by swapping each alphabet with its corresponding magical counterpart.

    Parameters:
    S (str): The input string to be converted.

    Returns:
    str: The magical version of the input string.
    """
    magical_string = ''
    for char in S:
        magical_char = chr(122 - (ord(char) - ord('a')))
        magical_string += magical_char
    return magical_string