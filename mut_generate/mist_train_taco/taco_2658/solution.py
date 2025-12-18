"""
QUESTION:
E869120 defined a sequence $a$ like this:


* $a_1=a_2=1$, $a_{k+2}=a_{k+1}+a_k \ (k \ge 1)$


He also defined sequences $d_1, d_2, d_3, \dots , d_n$, as the following recurrence relation :


* $d_{1, j} = a_j$
* $d_{i, j} = \sum_{k = 1}^j d_{i - 1, k} \ (i \ge 2)$


You are given integers $n$ and $m$. Please calculate the value of $d_{n, m}$.
Since the answer can be large number, print the answer modulo $998,244,353$.
Can you solve this problem???

Input

The input is given from standard input in the following format.



> $n \quad m$

Output

* Print $d_{n, m}$ modulo $998,244,353$.



Constraints

* $1 \le n \le 200,000$
* $1 \le m \le 10^{18}$



Subtasks

Subtask 1 [ $100$ points ]


* The testcase in this subtask satisfies $1 \le n, m \le 3,000$.

Subtask 2 [ $170$ points ]


* The testcase in this subtask satisfies $1 \le m \le 200,000$.

Subtask 3 [ $230$ points ]


* The testcase in this subtask satisfies $1 \le n \le 3$.

Subtask 4 [ $420$ points ]


* The testcase in this subtask satisfies $1 \le n \le 1000$.

Subtask 5 [ $480$ points ]


* There are no additional constraints.

Output

* Print $d_{n, m}$ modulo $998,244,353$.



Constraints

* $1 \le n \le 200,000$
* $1 \le m \le 10^{18}$



Subtasks

Subtask 1 [ $100$ points ]


* The testcase in this subtask satisfies $1 \le n, m \le 3,000$.

Subtask 2 [ $170$ points ]


* The testcase in this subtask satisfies $1 \le m \le 200,000$.

Subtask 3 [ $230$ points ]


* The testcase in this subtask satisfies $1 \le n \le 3$.

Subtask 4 [ $420$ points ]


* The testcase in this subtask satisfies $1 \le n \le 1000$.

Subtask 5 [ $480$ points ]


* There are no additional constraints.

Input

The input is given from standard input in the following format.



> $n \quad m$

Examples

Input

4 7


Output

176


Input

12 20


Output

174174144


Input

16 30


Output

102292850
"""

M = 998244353

def matrix_multiply(a, b):
    return [
        (a[0] * b[0] + a[1] * b[2]) % M,
        (a[0] * b[1] + a[1] * b[3]) % M,
        (a[2] * b[0] + a[3] * b[2]) % M,
        (a[2] * b[1] + a[3] * b[3]) % M
    ]

def fibonacci_matrix_power(n):
    e = [1, 0, 0, 1]
    z = [1, 1, 1, 0]
    while n:
        if n % 2 > 0:
            e = matrix_multiply(e, z)
        z = matrix_multiply(z, z)
        n //= 2
    return e[1]

def calculate_d_sequence(n, m):
    I = [1, 1]
    r = fibonacci_matrix_power(m + 2 * n - 2)
    c = 1
    for i in range(2, n):
        I += [(M - M // i) * I[M % i] % M]
    for i in range(n - 1):
        r = (r + c * (M - fibonacci_matrix_power(2 * n - 2 - 2 * i))) % M
        c = c * (m + i) * I[i + 1] % M
    return r