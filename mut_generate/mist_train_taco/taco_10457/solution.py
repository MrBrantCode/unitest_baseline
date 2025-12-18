"""
QUESTION:
There is a new mobile game that starts with consecutively numbered clouds.  Some of the clouds are thunderheads and others are cumulus.  The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus $\mbox{1}$ or $2$.  The player must avoid the thunderheads.  Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud.  It is always possible to win the game.  

For each game, you will get an array of clouds numbered $\mbox{0}$ if they are safe or $\mbox{1}$ if they must be avoided.  

Example 

$c=[0,1,0,0,0,1,0]$  

Index the array from $\boldsymbol{0\ldots6}$.  The number on each cloud is its index in the list so the player must avoid the clouds at indices $\mbox{I}$ and $5$.  They could follow these two paths: $0\rightarrow2\rightarrow4\rightarrow6$ or $0\to2\to3\to4\to6$.  The first path takes $3$ jumps while the second takes $\begin{array}{c}4\end{array}$.  Return $3$.

Function Description  

Complete the jumpingOnClouds function in the editor below.  

jumpingOnClouds has the following parameter(s):  

int c[n]: an array of binary integers  

Returns  

int: the minimum number of jumps required

Input Format

The first line contains an integer $n$, the total number of clouds. 
The second line contains $n$ space-separated binary integers describing clouds $c[i]$ where $0\leq i<n$.

Constraints

$2\leq n\leq100$
$c[i]\in\{0,1\}$
$c[0]=c[n-1]=0$

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0

Sample Output 0

4

Explanation 0: 

The player must avoid $c[2]$ and $c\left[5\right]$. The game can be won with a minimum of $\begin{array}{c}4\end{array}$ jumps:

Sample Input 1

6
0 0 0 0 1 0

Sample Output 1

3

Explanation 1: 

The only thundercloud to avoid is $c\left[4\right]$. The game can be won in $3$ jumps:
"""

def minimum_jumps(c: list[int]) -> int:
    n = len(c)
    res = 0
    i = 0
    
    while i < n - 1:
        if i + 2 < n and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        res += 1
    
    return res