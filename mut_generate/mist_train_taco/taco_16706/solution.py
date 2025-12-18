"""
QUESTION:
Martha is interviewing at Subway. One of the rounds of the interview requires her to cut a bread of size $l\times b$ into smaller identical pieces such that each piece is a square having maximum possible side length with no left over piece of bread.

Input Format

The first line contains an integer $\mathbf{T}$. $\mathbf{T}$ lines follow. Each line contains two space separated integers $\boldsymbol{l}$ and $\boldsymbol{b}$ which denote length and breadth of the bread. 

Constraints

$1\leq T\leq1000$
$1\leq l,b\leq1000$

Output Format

$\mathbf{T}$ lines, each containing an integer that denotes the number of squares of maximum size, when the bread is cut as per the given condition.

Sample Input 0
2
2 2
6 9

Sample Output 0
1
6

Explanation 0

The 1^{st} testcase has a bread whose original dimensions are $2\times2$, the bread is uncut and is a square. Hence the answer is 1. 

The 2^{nd} testcase has a bread of size $6\times9$. We can cut it into 54 squares of size $1\times1$, 6 of size $3\times3$. For other sizes we will have leftovers. Hence, the number of squares of maximum size that can be cut is 6.
"""

def calculate_maximum_squares(l, b):
    # Determine the smaller dimension to find the GCF
    if l > b:
        x = b
    else:
        x = l
    
    # Find the Greatest Common Factor (GCF)
    GCF = 1
    for i in range(1, x + 1):
        if l % i == 0 and b % i == 0:
            GCF = i
    
    # Calculate the number of maximum size squares
    return int(l * b / (GCF * GCF))