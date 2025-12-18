"""
QUESTION:
Read problem statements in [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

There are two types of vaccines available: Covaxin and Covishield.

A black marketeer has X coins and wants to buy as many vaccines as possible. Due to the black marketing concerns, government has enforced the following policy:

i^{th} dose of Covaxin costs a + (i - 1)\cdot b coins for every i ≥ 1. 

i^{th} dose of Covishield costs c + (i - 1)\cdot d coins for every i ≥ 1.

The values of the four parameters a, b, c and d, however isn't constant and might vary from query to query. In general the value of these four parameters for i^{th} query will be A_{i}, B_{i}, C_{i} and D_{i} respectively. 
Let ans_{i} be the maximum total quantity of vaccines the black marketeer can buy corresponding to the i^{th} query. For each query, you have to find the value of ans_{i}. 
 
You will be given integers A_{1}, B_{1}, C_{1}, D_{1}, P, Q, R, S, T and M which will define the queries to be followed. 

For i ≥ 1 and i ≤ I - 1:
A_{i+1} = (A_{i} + ans_{i}\cdot T) \bmod M + P
B_{i+1} = (B_{i} + ans_{i}\cdot T) \bmod M + Q 
C_{i+1} = (C_{i} + ans_{i}\cdot T) \bmod M + R 
D_{i+1} = (D_{i} + ans_{i}\cdot T) \bmod M + S .

Note: Since the output is large, prefer using fast input-output methods.

------ Input Format ------ 

- First line contains of input contains an integer I denoting the number of queries.
- Second line of input contains five integers X, A_{1}, B_{1}, C_{1}, D_{1}.
- Third line of input contains six integers P, Q, R, S, T, M.

------ Output Format ------ 

For each query output the maximum quantity of vaccines the black marketeer can buy.

------ Constraints ------ 

$1 ≤ I ≤ 5 \cdot 10^{5}$
$1 ≤ X,A_{1},B_{1},C_{1},D_{1} ≤ 10^{18}$
$1 ≤ P,Q,R,S,M ≤ 10^{18}$
$1 ≤ T ≤ 10^{9}$

------ subtasks ------ 

Subtask #1 (10 points): 
$1 ≤ I ≤ 10^{3}$
$1 ≤ X ≤ 10^{9}$
Time limit: $1$ sec 

Subtask #2 (30 points): 
$1 ≤ I ≤ 10^{3}$
$1 ≤ X ≤ 10^{15}$
$10^{9} ≤ A_{1} ≤ 10^{18}$
$10^{9} ≤ B_{1} ≤ 10^{18}$
$10^{9} ≤ P ≤ 10^{18}$
$10^{9} ≤ Q ≤ 10^{18}$
Time limit: $1$ sec 

Subtask #3 (60 points): 
Original constraints
Time limit: $3$ sec 

----- Sample Input 1 ------ 
3
20 2 3 4 1
3 7 8 4 11 20

----- Sample Output 1 ------ 
4
1
2

----- explanation 1 ------ 

Test case $1$: 
- For the first query, $[a, b, c, d] = [A_{1}, B_{1}, C_{1}, D_{1}] = [2, 3, 4, 1]$. It is optimal to buy $2$ doses of Covaxin $(2+5=7)$ and $2$ doses of Covishield $(4+5=9)$. So the total money spent is $7+9=16$ and now the black marketeer cannot buy any more doses. So the answer is 4.

- For the second query, $[a, b, c, d] = [A_{2}, B_{2}, C_{2}, D_{2}] = [(2 + 11\cdot 4)\bmod 20 + 3, (3 + 11\cdot 4) \bmod 20 + 7, (4 + 11\cdot 4) \bmod 20 + 8, (1 + 11\cdot 4) \bmod 20 + 4]=[9, 14, 16, 9]$. 

- For the third and the last query, $[a, b, c, d] = [A_{3}, B_{3}, C_{3}, D_{3}] = [3, 12, 15, 4]$.
"""

import cmath

def calculate_max_vaccines(I, X, A1, B1, C1, D1, P, Q, R, S, T, M):
    def find_total(x, y):
        return B * x * x / 2 + j * x + D * y * y / 2 + k * y

    def find_root(a, b, c):
        dis = b ** 2 - 4 * a * c
        r1 = (-b - cmath.sqrt(dis)) / (2 * a)
        r2 = (-b + cmath.sqrt(dis)) / (2 * a)
        return max(r1.real, r2.real)

    results = []
    A, B, C, D = A1, B1, C1, D1

    for _ in range(I):
        i = (2 * (A - C) + D - B) / (2 * D)
        j = A - B / 2
        k = C - D / 2
        a = B / 2 * (B / D + 1)
        b = j + B * k / D + B * i
        c = i * k + D * i * i / 2 - X
        r = find_root(a, b, c)
        y = r * B / D + i
        (r, y) = (int(r), int(y))
        arr = [(r + i, y + j) for i in range(2) for j in range(2)]
        cx = int(find_root(B / 2, j, -X))
        remain = X - find_total(cx, 0)
        arr.append((cx, int(find_root(D / 2, k, -remain))))
        csd = int(find_root(D / 2, k, -X))
        remain = X - find_total(0, csd)
        arr.append((int(find_root(B / 2, j, -remain)), csd))
        ans = max(map(lambda y: y[0] + y[1], filter(lambda x: x[0] >= 0 and x[1] >= 0 and (find_total(x[0], x[1]) <= X), arr)))
        results.append(ans)
        A = (A + ans * T) % M + P
        B = (B + ans * T) % M + Q
        C = (C + ans * T) % M + R
        D = (D + ans * T) % M + S

    return results