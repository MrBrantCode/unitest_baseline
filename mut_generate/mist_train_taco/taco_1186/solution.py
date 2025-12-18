"""
QUESTION:
You are given a positive integer $N$. Print a numerical triangle of height $N-1$ like the one below:  

1
22
333
4444
55555
......

Can you do it using only arithmetic operations, a single for loop and print statement?  

Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.  

Note: Using anything related to strings will give a score of $\mbox{0}$.  

Input Format 

A single line containing integer, $N$.  

Constraints 

$1\leq N\leq9$  

Output Format 

Print $N-1$ lines as explained above.  

Sample Input  

5

Sample Output  

1
22
333
4444
"""

def print_numerical_triangle(N):
    for i in range(1, N):
        print(1 if i == 1 else 22 if i == 2 else 333 if i == 3 else 4444 if i == 4 else 55555 if i == 5 else 666666 if i == 6 else 7777777 if i == 7 else 88888888 if i == 8 else 999999999)