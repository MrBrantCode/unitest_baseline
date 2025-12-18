"""
QUESTION:
Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring $\text{"010"}$. 

In one step, Alice can change a $0$ to a $1$ or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

Example    

$b=\textbf{010}$    

She can change any one element and have a beautiful string.

Function Description  

Complete the beautifulBinaryString function in the editor below.   

beautifulBinaryString has the following parameter(s):  

string b: a string of binary digits   

Returns   

int: the minimum moves required

Input Format

The first line contains an integer $n$, the length of binary string. 

The second line contains a single binary string $\boldsymbol{b}$.

Constraints

$1\leq n\leq100$
$b[i]\in\{0,1\}$.

Output Format

Print the minimum number of steps needed to make the string beautiful.

Sample Input 0

STDIN       Function
-----       --------
7           length of string n = 7
0101010     b = '0101010'

Sample Output 0

2  

Explanation 0: 

In this sample, $b=\text{"0101010"}$

The figure below shows a way to get rid of each instance of $\text{"010"}$:

Make the string beautiful by changing $2$ characters ($b[2]$ and $b\left[5\right]$).

Sample Input 1

5
01100

Sample Output 1

0

Sample Case 1:

In this sample $b=\text{"01100"}$     

Explanation 1

The substring $\text{"010"}$ does not occur in $\boldsymbol{b}$, so the string is already beautiful in $0$ moves.

Sample Input 2

10
0100101010

Sample Output 2

3

Explanation 2  

In this sample $b=\text{"0100101010"}$

One solution is to change the values of $b[2],b[5]\:\text{and}\:b[9]$ to form a beautiful string.
"""

import re

def beautifulBinaryString(b: str) -> int:
    """
    Counts the minimum number of steps needed to make the binary string beautiful.
    
    A binary string is considered beautiful if it does not contain the substring "010".
    In one step, a character in the string can be changed from '0' to '1' or from '1' to '0'.
    
    Parameters:
    b (str): A string of binary digits.
    
    Returns:
    int: The minimum number of steps required to make the string beautiful.
    """
    return len(re.findall('010', b))