"""
QUESTION:
Chef's new friend hErd gave him two functions f and g.

The function f is defined over x (x≥ 1) as:  

f(x) = \begin{cases}
0, & \text{if } x = 1 \\
f( \frac{x}{2} ) + 1, & \text{if } x \text{ is even} \\
f( \lfloor \frac{x}{2} \rfloor ), & \text{if } x \text{ is odd} \\
\end{cases}

The function g is defined over x (x≥ 1) as:  

g(x) = \begin{cases}
1, & \text{if } x = 1 \\
2\cdot g( \frac{x}{2} ) + 1, & \text{if } x \text{ is even} \\
2\cdot g( \lfloor \frac{x}{2} \rfloor ), & \text{if } x \text{ is odd} \\
\end{cases}

where \lfloor z \rfloor, denotes the greatest integer less than or equal to z.

He also gave Chef two integers L and R. Chef has to find the maximum value of f(x)+g(x) for L ≤ x ≤ R.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- The only line of each test case contains two space-separated integers L and R, as mentioned in the statement.

------ Output Format ------ 

For each test case, output on a new line the maximum value of f(x)+g(x) for L ≤ x ≤ R.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ L ≤ R ≤ 10^{9}$

----- Sample Input 1 ------ 
3
1 1
1 2
1 20
----- Sample Output 1 ------ 
1
4
35
----- explanation 1 ------ 
Test case $1$: $f(1)=0$ and $g(1)=1$. Hence, $f(x) + g(x) = 1$.

Test case $2$: There are $2$ possible values of $x$.
- $x = 1$: $f(1)+g(1)=1$ 
- $x = 2$: $f(2)+g(2)=(f(1) + 1) + (2\cdot g(1) + 1) = 1 + 3 = 4$.

Hence the maximum value of $f(x) + g(x) = 4$.
"""

def max_f_plus_g(L, R):
    def base_2(x):
        return bin(x)[2:]

    def f_plus_g(x):
        b = base_2(x)
        k = len(b) - 1
        c = b.count('0')
        return c + 2 ** (k + 1) + 2 ** k - 1 - x

    k = len(base_2(R)) - 1
    if 2 ** k >= L:
        return k + 2 ** (k + 1) - 1

    x = L
    mx = 0
    while x <= R:
        mx = max(mx, f_plus_g(x))
        i = (x ^ (x - 1)).bit_length() - 1
        x += 2 ** i

    return mx