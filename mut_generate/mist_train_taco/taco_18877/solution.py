"""
QUESTION:
Given a sequence of $n$ integers, $p(1),p(2),...,p(n)$ where each element is distinct and satisfies $1\leq p(x)\leq n$. For each $\boldsymbol{x}$ where $1\leq x\leq n$, that is $\boldsymbol{x}$ increments from $\mbox{1}$ to $n$, find any integer $y$ such that $p(p(y))\equiv x$ and keep a history of the values of $y$ in a return array.

Example   

$p=[5,2,1,3,4]$    

Each value of $\boldsymbol{x}$ between $\mbox{1}$ and $5$, the length of the sequence, is analyzed as follows:

$x=1\equiv p[3],p[4]=3$, so $p[p[4]]=1$
$x=2\equiv p[2],p[2]=2$, so $p[p[2]]=2$
$x=3\equiv p[4],p[5]=4$, so $p[p[5]]=3$
$x=4\equiv p[5],p[1]=5$, so $p[p[1]]=4$
$x=5\equiv p[1],p[3]=1$, so $p[p[3]]=5$

The values for $y$ are $[4,2,5,1,3]$.  

Function Description  

Complete the permutationEquation function in the editor below.   

permutationEquation has the following parameter(s):  

int p[n]: an array of integers  

Returns   

int[n]: the values of $y$ for all $\boldsymbol{x}$ in the arithmetic sequence $\mbox{1}$ to $n$

Input Format

The first line contains an integer $n$, the number of elements in the sequence. 

The second line contains $n$ space-separated integers $p[i]$ where $1\leq i\leq n$.

Constraints

$1\leq n\leq50$
$1\leq p[i]\leq50$, where $1\leq i\leq n$.
Each element in the sequence is distinct.

Sample Input 0
3
2 3 1

Sample Output 0
2
3
1

Explanation 0

Given the values of $p(1)=2$, $p(2)=3$, and $p(3)=1$, we calculate and print the following values for each $\boldsymbol{x}$ from $\mbox{1}$ to $n$:

$x=1\equiv p(3)=p(p(2))=p(p(y))$, so we print the value of $y=2$ on a new line.
$x=2\equiv p(1)=p(p(3))=p(p(y))$, so we print the value of $y=3$ on a new line.
$x=3\equiv p(2)=p(p(1))=p(p(y))$, so we print the value of $y=1$ on a new line.

Sample Input 1
5
4 3 5 1 2

Sample Output 1
1
3
5
4
2
"""

def permutation_equation(p):
    n = len(p)
    y_values = []
    
    for x in range(1, n + 1):
        for y in range(n):
            if p[p[y] - 1] == x:
                y_values.append(y + 1)
                break
    
    return y_values