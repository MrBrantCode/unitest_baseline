"""
QUESTION:
In mathematics, the [degree] of polynomials in one variable is the highest power of the variable in the algebraic expression with non-zero coefficient.

Chef has a polynomial in one variable x with N terms. The polynomial looks like A_{0}\cdot x^{0} + A_{1}\cdot x^{1} + \ldots + A_{N-2}\cdot x^{N-2} + A_{N-1}\cdot x^{N-1} where A_{i-1} denotes the coefficient of the i^{th} term x^{i-1} for all (1≤ i≤ N). 

Find the degree of the polynomial.

Note: It is guaranteed that there exists at least one term with non-zero coefficient.

------ Input Format ------ 

- First line will contain T, number of test cases. Then the test cases follow.
- First line of each test case contains of a single integer N - the number of terms in the polynomial.
- Second line of each test case contains of N space-separated integers - the i^{th} integer A_{i-1} corresponds to the coefficient of x^{i-1}.

------ Output Format ------ 

For each test case, output in a single line, the degree of the polynomial.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 1000$
$-1000 ≤A_{i} ≤1000$
$A_{i} \ne 0$ for at least one $(0≤i < N)$.

----- Sample Input 1 ------ 
4
1
5
2
-3 3
3
0 0 5
4
1 2 4 0

----- Sample Output 1 ------ 
0
1
2
2
----- explanation 1 ------ 
Test case $1$: There is only one term $x^{0}$ with coefficient $5$. Thus, we are given a constant polynomial and the degree is $0$.

Test case $2$: The polynomial is $-3\cdot x^{0} + 3\cdot x^{1} = -3 + 3\cdot x$. Thus, the highest power of $x$ with non-zero coefficient is $1$.

Test case $3$: The polynomial is $0\cdot x^{0} + 0\cdot x^{1} + 5\cdot x^{2}= 0+0 + 5\cdot x^{2}$. Thus, the highest power of $x$ with non-zero coefficient is $2$.

Test case $4$: The polynomial is $1\cdot x^{0} + 2\cdot x^{1}+ 4\cdot x^{2} + 0\cdot x^{3}= 1 + 2\cdot x + 4\cdot x^{2}$. Thus, the highest power of $x$ with non-zero coefficient is $2$.
"""

def find_polynomial_degree(coefficients):
    reduce = 0
    for i in range(len(coefficients)):
        if coefficients[-1 - i] == 0:
            reduce += 1
        else:
            break
    return len(coefficients) - 1 - reduce