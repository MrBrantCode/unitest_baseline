"""
QUESTION:
A word from the English dictionary is taken and arranged as a matrix. e.g. "MATHEMATICS"

MATHE  
ATHEM  
THEMA  
HEMAT  
EMATI  
MATIC  
ATICS  

There are many ways to trace this matrix in a way that helps you construct this word. You start tracing the matrix from the top-left position and at each iteration, you either move RIGHT or DOWN, and ultimately reach the bottom-right of the matrix. It is assured that any such tracing generates the same word. How many such tracings can be possible for a given
word of length m+n-1 written as a matrix of size m * n?

Input Format 

The first line of input contains an integer T. T test cases follow. 

Each test case contains 2 space separated integers m & n (in a new line) indicating that the matrix has m rows and each row has n characters.  

Constraints 

1 <= T <= 10^{3} 

1 ≤ m,n ≤ 10^{6}

Output Format 

Print the number of ways (S) the word can be traced as explained in the problem statement.
If the number is larger than 10^{9}+7, 

print  S mod (10^9 + 7) for each testcase (in a new line). 

Sample Input

1
2 3

Sample Output

3

Explanation 

Let's consider a word AWAY written as the matrix

AWA
WAY

Here, the word AWAY can be traced in 3 different ways, traversing either RIGHT or DOWN.

AWA
  Y

AW
 AY

A
WAY

Hence the answer is 3.

Timelimit
Time limit for this challenge is given here
"""

def count_matrix_tracings(m: int, n: int) -> int:
    """
    Calculate the number of ways to trace a matrix of size m x n from the top-left to the bottom-right,
    moving only right or down, and return the result modulo 10^9 + 7.

    Parameters:
    m (int): Number of rows in the matrix.
    n (int): Number of columns in the matrix.

    Returns:
    int: Number of ways to trace the matrix modulo 10^9 + 7.
    """
    MOD = 1000000007

    def modinv(n, p):
        return pow(n, p - 2, p)

    def mod_choose(n, k, m):
        if k < 0 or k > n:
            return 0
        else:
            (p, q) = (1, 1)
            for i in range(1, min(k, n - k) + 1):
                p = p * n % m
                q = q * i % m
                n -= 1
            return p * modinv(q, m) % m

    return mod_choose(n + m - 2, m - 1, MOD)