"""
QUESTION:
You are given an array $a$ of length $n$ and array $b$ of length $m$ both consisting of only integers $0$ and $1$. Consider a matrix $c$ of size $n \times m$ formed by following rule: $c_{i, j} = a_i \cdot b_j$ (i.e. $a_i$ multiplied by $b_j$). It's easy to see that $c$ consists of only zeroes and ones too.

How many subrectangles of size (area) $k$ consisting only of ones are there in $c$?

A subrectangle is an intersection of a consecutive (subsequent) segment of rows and a consecutive (subsequent) segment of columns. I.e. consider four integers $x_1, x_2, y_1, y_2$ ($1 \le x_1 \le x_2 \le n$, $1 \le y_1 \le y_2 \le m$) a subrectangle $c[x_1 \dots x_2][y_1 \dots y_2]$ is an intersection of the rows $x_1, x_1+1, x_1+2, \dots, x_2$ and the columns $y_1, y_1+1, y_1+2, \dots, y_2$.

The size (area) of a subrectangle is the total number of cells in it.


-----Input-----

The first line contains three integers $n$, $m$ and $k$ ($1 \leq n, m \leq 40\,000, 1 \leq k \leq n \cdot m$), length of array $a$, length of array $b$ and required size of subrectangles.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($0 \leq a_i \leq 1$), elements of $a$.

The third line contains $m$ integers $b_1, b_2, \ldots, b_m$ ($0 \leq b_i \leq 1$), elements of $b$.


-----Output-----

Output single integer — the number of subrectangles of $c$ with size (area) $k$ consisting only of ones.


-----Examples-----
Input
3 3 2
1 0 1
1 1 1

Output
4

Input
3 5 4
1 1 1
1 1 1 1 1

Output
14



-----Note-----

In first example matrix $c$ is:

 $\left(\begin{array}{l l l}{1} & {1} & {1} \\{0} & {0} & {0} \\{1} & {1} & {1} \end{array} \right)$ 

There are $4$ subrectangles of size $2$ consisting of only ones in it:

 [Image] 

In second example matrix $c$ is:

 $\left(\begin{array}{l l l l l}{1} & {1} & {1} & {1} & {1} \\{1} & {1} & {1} & {1} & {1} \\{1} & {1} & {1} & {1} & {1} \end{array} \right)$
"""

def count_subrectangles(n, m, k, a, b):
    arr = [0] * (n + 1)
    brr = [0] * (m + 1)
    
    for i in range(1, n + 1):
        arr[i] = a[i - 1] + arr[i - 1]
    
    for i in range(1, m + 1):
        brr[i] = b[i - 1] + brr[i - 1]
    
    ans = 0
    
    for f in range(1, int(k ** 0.5) + 1):
        if k % f == 0:
            x = f
            y = k // f
            if y <= m:
                cc = 0
                for i in range(n + 1):
                    if i + x > n:
                        break
                    if arr[i + x] - arr[i] == x:
                        cc += 1
                bb = 0
                for i in range(m + 1):
                    if i + y > m:
                        break
                    if brr[i + y] - brr[i] == y:
                        bb += 1
                ans += cc * bb
            if x != y:
                y = f
                x = k // f
                cc = 0
                for i in range(n + 1):
                    if i + x > n:
                        break
                    if arr[i + x] - arr[i] == x:
                        cc += 1
                bb = 0
                for i in range(m + 1):
                    if i + y > m:
                        break
                    if brr[i + y] - brr[i] == y:
                        bb += 1
                ans += cc * bb
    
    return ans