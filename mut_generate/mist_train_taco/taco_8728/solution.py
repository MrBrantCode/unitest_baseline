"""
QUESTION:
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

Example 

$n=7$ 

$ar=[1,2,1,2,1,3,2]$   

There is one pair of color $\mbox{I}$ and one of color $2$.  There are three odd socks left, one of each color.  The number of pairs is $2$.  

Function Description  

Complete the sockMerchant function in the editor below.     

sockMerchant has the following parameter(s):  

int n: the number of socks in the pile   
int ar[n]: the colors of each sock   

Returns   

int: the number of pairs   

Input Format

The first line contains an integer $n$, the number of socks represented in $\boldsymbol{ar}$. 

The second line contains $n$ space-separated integers, $ar[i]$, the colors of the socks in the pile.

Constraints

$1\leq n\leq100$
$1\leq ar[i]\leq100$ where $0\leq i<n$

Sample Input
STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

Sample Output
3

Explanation

There are three pairs of socks.
"""

from collections import Counter

def sockMerchant(n, ar):
    # Count the frequency of each sock color
    sock_counts = Counter(ar)
    
    # Calculate the number of pairs
    pairs = 0
    for color in sock_counts:
        pairs += sock_counts[color] // 2
    
    return pairs