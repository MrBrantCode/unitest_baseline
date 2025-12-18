"""
QUESTION:
Happy Ladybugs is a board game having the following properties:

The board is represented by a string, $\boldsymbol{b}$, of length $n$. The $i^{\mbox{th}}$ character of the string, $b[i]$, denotes the $i^{\mbox{th}}$ cell of the board.

If $b[i]$ is an underscore (i.e., _), it means the $i^{\mbox{th}}$ cell of the board is empty.
If $b[i]$ is an uppercase English alphabetic letter (ascii[A-Z]), it means the $i^{\mbox{th}}$ cell contains a ladybug of color $b[i]$.
String $\boldsymbol{b}$ will not contain any other characters.
A ladybug is happy only when its left or right adjacent cell (i.e., $b[i\pm1]$) is occupied by another ladybug having the same color.
In a single move, you can move a ladybug from its current position to any empty cell. 

Given the values of $n$ and $\boldsymbol{b}$ for $\mathrm{~g~}$ games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, return YES if all the ladybugs can be made happy through some number of moves.  Otherwise, return NO. 

Example 

$b=[YYR\text{_}B\text{_}BR]$    

You can move the rightmost $\mbox{B}$ and $\mbox{R}$ to make $b=[YYRRBB\text{__}]$ and all the ladybugs are happy. Return YES.   

Function Description  

Complete the happyLadybugs function in the editor below.   

happyLadybugs has the following parameters:

string b: the initial positions and colors of the ladybugs   

Returns   

string: either YES or NO   

Input Format

The first line contains an integer $\mathrm{~g~}$, the number of games.  

The next $\mathrm{~g~}$ pairs of lines are in the following format:  

The first line contains an integer $n$, the number of cells on the board.  
The second line contains a string $\boldsymbol{b}$ that describes the $n$ cells of the board.  

Constraints

$1\leq g,n\leq100$  
$b[i]\in\{\_,ascii[A-Z]\}$

Sample Input 0
4
7
RBY_YBR
6
X_Y__X
2
__
6
B_RRBR

Sample Output 0
YES
NO
YES
YES

Explanation 0

The four games of Happy Ladybugs are explained below:

Initial board: 

After the first move: 

After the second move: 

After the third move: 

Now all the ladybugs are happy, so we print YES on a new line.
There is no way to make the ladybug having color Y happy, so we print NO on a new line.
There are no unhappy ladybugs, so we print YES on a new line.
Move the rightmost $\mbox{B}$ and $\mbox{R}$ to form $b=[BBRR\text{__}]$.

Sample Input 1
5
5
AABBC
7
AABBC_C
1
_
10
DD__FQ_QQF
6
AABCBC

Sample Output 1
NO
YES
YES
YES
NO
"""

import collections

def can_ladybugs_be_happy(b):
    def all_happy(ladybugs):
        for (i, bug) in enumerate(ladybugs):
            try:
                left = ladybugs[i - 1]
            except IndexError:
                left = None
            try:
                right = ladybugs[i + 1]
            except IndexError:
                right = None
            if bug not in (left, right):
                return False
        return True
    
    counter = collections.Counter(b)
    empty_cells = counter['_']
    del counter['_']
    
    if 1 in counter.values():
        return 'NO'
    elif empty_cells == 0 and (not all_happy(b)):
        return 'NO'
    else:
        return 'YES'