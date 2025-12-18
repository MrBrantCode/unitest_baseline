"""
QUESTION:
A person is getting ready to leave and needs a pair of matching socks.  If there are $n$ colors of socks in the drawer, how many socks need to be removed to be certain of having a matching pair?  

Example
$n=2$  

There are $2$ colors of socks in the drawer.  If they remove $2$ socks, they may not match.  The minimum number to insure success is $3$.  

Function Description  

Complete the maximumDraws function in the editor below.  

maximumDraws has the following parameter:  

int n: the number of colors of socks  

Returns  

int: the minimum number of socks to remove to guarantee a matching pair. 

Input Format 

The first line contains the number of test cases, $\boldsymbol{\boldsymbol{t}}$. 

Each of the following $\boldsymbol{\boldsymbol{t}}$ lines contains an integer $n$.

Constraints 

$1\leq t\leq1000$ 

$0<n<10^6$  

Sample Input

2
1
2

Sample Output

2
3

Explanation 

Case 1 : Only 1 color of sock is in the drawer.  Any $2$ will match. 

Case 2 : 2 colors of socks are in the drawer. The first two removed may not match.  At least $3$ socks need to be removed to guarantee success.
"""

def maximum_draws(n: int) -> int:
    """
    Calculate the minimum number of socks to remove to guarantee a matching pair.

    Parameters:
    n (int): The number of colors of socks in the drawer.

    Returns:
    int: The minimum number of socks to remove to guarantee a matching pair.
    """
    return n + 1