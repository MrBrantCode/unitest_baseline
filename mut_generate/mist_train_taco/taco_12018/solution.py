"""
QUESTION:
Check Tutorial tab to know how to to solve.  

You are given a string $\mbox{S}$ and width $\boldsymbol{w}$. 

Your task is to wrap the string into a paragraph of width $\boldsymbol{w}$.  

Function Description   

Complete the wrap function in the editor below.  

wrap has the following parameters:   

string string: a long string   
int max_width: the width to wrap to   

Returns   

string: a single string with newline characters ('\n') where the breaks should be   

Input Format

The first line contains a string, $\textit{string}$. 

The second line contains the width, $max_width$.

Constraints

$0<len(string)<1000$  
$0<max_{w}idth<len(string)$

Sample Input 0
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output 0
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""

def wrap_string(string: str, max_width: int) -> str:
    """
    Wraps the given string into a paragraph of the specified width.

    Parameters:
    - string (str): The input string to be wrapped.
    - max_width (int): The maximum width of each line after wrapping.

    Returns:
    - str: A single string with newline characters ('\n') where the breaks should be.
    """
    return '\n'.join([string[i * max_width:(i + 1) * max_width] for i in range(int(len(string) / max_width) + 1)])