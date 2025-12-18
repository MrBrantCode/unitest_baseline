"""
QUESTION:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.  

For example, the square matrix $\textbf{arr}$ is shown below:  

1 2 3
4 5 6
9 8 9  

The left-to-right diagonal = $1+5+9=15$.  The right to left diagonal = $3+5+9=17$.  Their absolute difference is $|15-17|=2$.  

Function description

Complete the $\textit{diagonalDifference}$ function in the editor below.  

diagonalDifference takes the following parameter:  

int arr[n][m]: an array of integers 

Return  

int: the absolute diagonal difference  

Input Format

The first line contains a single integer, $n$,  the number of rows and columns in the square matrix $\textbf{arr}$. 

Each of the next $n$ lines describes a row, $arr\left[i\right]$, and consists of $n$ space-separated integers $ar r[i][j]$.

Constraints

$-100\leq arr[i][j]\leq100$

Output Format

Return the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input
3
11 2 4
4 5 6
10 8 -12

Sample Output
15

Explanation

The primary diagonal is:  

11
   5
     -12

Sum across the primary diagonal: 11 + 5 - 12 = 4 

The secondary diagonal is:

     4
   5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19 

Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
"""

def diagonal_difference(arr):
    n = len(arr)  # Since it's a square matrix, the number of rows is equal to the number of columns
    sum1 = 0  # Sum of the primary diagonal
    sum2 = 0  # Sum of the secondary diagonal
    
    for i in range(n):
        sum1 += arr[i][i]  # Primary diagonal elements
        sum2 += arr[i][n - 1 - i]  # Secondary diagonal elements
    
    return abs(sum1 - sum2)