"""
QUESTION:
Since you know how to compute large Fibonacci numbers quickly using matrix exponentiation, let's take things to the next level.  

Let $\boldsymbol{\alpha}$, $\boldsymbol{b}$, $\textbf{C}$, $\boldsymbol{d}$, $\boldsymbol{\mathrm{~e~}}$, $\mbox{f}$, $\mathrm{~g~}$ and $\mbox{h}$ be positive integers. We define two bi-infinite sequences
$(\ldots,x_{-2},x_{-1},x_{0},x_{1},x_{2},\ldots)$
and
$(\ldots,y_{-2},y_{-1},y_{0},y_{1},y_{2},\ldots)$
as follows:  

$x_n=\begin{cases}x_{n-a}+y_{n-b}+y_{n-c}+n\cdot d^n&\text{if}\ n\geq0\\ 1&\text{if}\ n<0\end{cases}$

and  

$y_n=\begin{cases}y_{n-e}+x_{n-f}+x_{n-g}+n\cdot h^n&\text{if}\ n\geq0\\ 1&\text{if}\ n<0\end{cases}$

Given $n$ and the eight integers above, find $x_n$ and $y_n$. Since these values can be very large, output them modulo $\mathbf{10^{9}}$.  

This link may help you get started: http://fusharblog.com/solving-linear-recurrence-for-programming-contest/

Input Format

The first line of input contains $\mathbf{T}$, the number of test cases. 

Each test case consists of a single line containing nine space separated integers: $\boldsymbol{\alpha}$, $\boldsymbol{b}$, $\textbf{C}$, $\boldsymbol{d}$, $\boldsymbol{\mathrm{~e~}}$, $\mbox{f}$, $\mathrm{~g~}$, $\mbox{h}$ and $n$, respectively.  

Constraints 

$1\leq T\leq100$ 

$1\leq a,b,c,d,e,f,g,h<10$ 

$1\leq n\leq10^{18}$  

Output Format

For each test case, output a single line containing two space separated integers, $x_n\:\text{mod}\:10^9$ and $y_n\:\text{mod}\:10^9$.  

Sample Input
3
1 2 3 1 1 2 3 1 10
1 2 3 2 2 1 1 4 10
1 2 3 4 5 6 7 8 90

Sample Output
1910 1910
909323 11461521
108676813 414467031

Explanation

In the second test case, the following is a table of values $x_i$ and $y_i$ for $0\leq i\leq10$:  

$\begin{array}{c|ccc}i&x_i&y_i&y_i\\ \hline0&3&11\\ 1&7&11\\ 2&19&41\\ 3&187&141\\ 4&1831&197\\ 5&631&5793\\ 6&2443&27097\\ 7&10249&125297\\ 8&40245&571811\\ 9&201975&2574881\\ 10&919373&14674881\\ \end{array}$

Remember that $x_i=y_i=1$ if $i<0$.  

One can verify this table by using the definition above. For example: 

$\begin{aligned}x_5&=x_{5-1}+y_{5-2}+y_{5-3}+y_{-3}+5\cdot2^5\\ &=x_{4}+y_{3}+y_{2}+160\\ &=81+241+49+160\\ y_6&=y_{5-2}+x_{5-1}+x_{5-1}+5\cdot4^5\\ &=y_{5-2}+x_{5-1}+x_{4}+x_{5-1}+5\cdot4^5\\ &=21+x_{4}+x_{4}+x_{5}+5120\\ &=5721+161+181+5120\\ &=x_{2-1}+y_{4-2}+y_{2-3}+2\cdot2^2\\ &=x_{1-1}+y_{0}+y_{4-1}+y_{2}+2\cdot2^2\\ &=7+3+1+8\\ \end{aligned}$
"""

def compute_fibonacci_like_sequences(a, b, c, d, e, f, g, h, n):
    """
    Computes the values of x_n and y_n for given parameters using matrix exponentiation.

    Parameters:
    a, b, c, d, e, f, g, h (int): Positive integers defining the sequences.
    n (int): The index for which to compute x_n and y_n.

    Returns:
    tuple: A tuple containing two integers (x_n % 10^9, y_n % 10^9).
    """
    from operator import mul

    def matrixMult(m1, m2, d):
        m2tr = list(zip(*m2))
        return [[sum(map(mul, m1row, m2col)) % d for m2col in m2tr] for m1row in m1]

    def matrixVectorMult(m, v):
        return [sum(map(mul, mrow, v)) for mrow in m]

    def matrixPowMod(mat, p, d):
        dim = len(mat)
        cur = [[i == j and 1 or 0 for j in range(dim)] for i in range(dim)]
        for c in bin(p)[2:]:
            cur = matrixMult(cur, cur, d)
            if c == '1':
                cur = matrixMult(cur, mat, d)
        return cur

    modulo = 10 ** 9
    mat = [[0] * 22 for i in range(22)]
    mat[0][1] = mat[1][2] = mat[2][3] = mat[3][4] = mat[4][5] = mat[5][6] = mat[6][7] = mat[7][8] = 1
    mat[8][9 - a] += 1
    mat[8][20 - b] += 1
    mat[8][20 - c] += 1
    mat[8][9] = mat[8][10] = mat[9][9] = mat[9][10] = mat[10][10] = d
    mat[11][12] = mat[12][13] = mat[13][14] = mat[14][15] = mat[15][16] = mat[16][17] = mat[17][18] = mat[18][19] = 1
    mat[19][20 - e] += 1
    mat[19][9 - f] += 1
    mat[19][9 - g] += 1
    mat[19][20] = mat[19][21] = mat[20][20] = mat[20][21] = mat[21][21] = h
    vec = [1] * 22
    vec[8] = vec[19] = 3
    vec[9] = vec[20] = 0
    resultVec = matrixVectorMult(matrixPowMod(mat, n, modulo), vec)
    return resultVec[8] % modulo, resultVec[19] % modulo