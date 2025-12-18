"""
QUESTION:
There are N bags, each containing two white balls. The i-th box contains two balls with integers x_i and y_i written on them, respectively.
For each of these bags, you will paint one of the balls red, and paint the other blue.
Afterwards, the 2N balls will be classified according to color.
Then, we will define the following:
 - R_{max}: the maximum integer written on a ball painted in red
 - R_{min}: the minimum integer written on a ball painted in red
 - B_{max}: the maximum integer written on a ball painted in blue
 - B_{min}: the minimum integer written on a ball painted in blue
Find the minimum possible value of (R_{max} - R_{min}) \times (B_{max} - B_{min}).

-----Constraints-----
 - 1 ≤ N ≤ 200,000
 - 1 ≤ x_i, y_i ≤ 10^9

-----Input-----
Input is given from Standard Input in the following format:
N
x_1 y_1
x_2 y_2
:
x_N y_N

-----Output-----
Print the minimum possible value.

-----Sample Input-----
3
1 2
3 4
5 6

-----Sample Output-----
15

The optimal solution is to paint the balls with x_1, x_2, y_3 red, and paint the balls with y_1, y_2, x_3 blue.
"""

def calculate_min_value(N, balls):
    L = []
    R = []
    LR = []
    INF = 10 ** 9 + 1
    m = INF
    M = 0
    
    for x, y in balls:
        if x > y:
            x, y = y, x
        L.append(x)
        R.append(y)
        LR.append((x, y))
        if m > x:
            m = x
            idx_m = len(L) - 1
        if M < y:
            M = y
            idx_M = len(R) - 1
    
    ans1 = (M - min(R)) * (max(L) - m)
    
    if idx_m == idx_M:
        return ans1
    
    a, b = L[idx_M], R[idx_m]
    if a > b:
        a, b = b, a
    
    LR = sorted([lr for i, lr in enumerate(LR) if i != idx_m and i != idx_M])
    
    if not LR:
        return ans1
    
    L, R = zip(*LR)
    max_R = [-1] * (N - 2)
    min_R = [-1] * (N - 2)
    max_R[0] = R[0]
    min_R[0] = R[0]
    
    for i in range(N - 3):
        max_R[i + 1] = max(max_R[i], R[i + 1])
        min_R[i + 1] = min(min_R[i], R[i + 1])
    
    l_min, l_max = L[0], L[-1]
    ans2 = max(b, l_max) - min(a, l_min)
    
    for i in range(N - 2):
        if i < N - 3:
            l_min = min(min_R[i], L[i + 1])
        else:
            l_min = min_R[i]
        l_max = max(l_max, max_R[i])
        ans2 = min(ans2, max(b, l_max) - min(a, l_min))
    
    ans2 *= M - m
    ans = min(ans1, ans2)
    
    return ans