"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef got interested in bits and wanted to learn about them, so his friend Pintu gave him a special function $F(X,Y,Z) = (X \wedge Z) \cdot (Y \wedge Z)$, where $\wedge$ is the [bitwise AND] operator and $X, Y, Z$ are non-negative integers.

Pintu wants Chef to maximise the function $F(X,Y,Z)$ for given $X$ and $Y$ by choosing an appropriate $Z$. However, to make it interesting, Pintu also gave Chef limits $L$ and $R$ for $Z$. In other words, he wants Chef to find a non-negative integer $Z$ ($L ≤ Z ≤ R$) such that $F(X,Y,Z) = \mathrm{max}_{L ≤ k ≤ R} ( F(X,Y,k) )$. If there is more than one such value of $Z$, he should find the smallest one in the range $[L, R]$.

Since Chef is busy cooking in the kitchen, he needs you to help him solve this problem.

Note: $X$, $Y$, $L$ and $R$ are chosen in such a way that $\mathrm{max}_{L ≤ k ≤ R} ( F(X,Y,k) )$ never exceeds $2^{62}$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains four space-separated integers $X$, $Y$, $L$ and $R$.

------  Output ------
For each test case, print a single line containing one integer ― the smallest value of $Z$ in the given range that maximises $F$.

------  Constraints ------
$1 ≤ T ≤ 10^{5}$
$0 ≤ X,Y ≤ 10^{12}$
$0 ≤ L ≤ R ≤ 10^{12}$

------  Subtasks ------
Subtask #1 (15 points):
$L = 0$
$R ≥ 2 \cdot \mathrm{max}(X,Y)$

Subtask #2 (25 points): $L = 0$

Subtask #3 (60 points): original constraints

----- Sample Input 1 ------ 
2

7 12 4 17

7 12 0 8
----- Sample Output 1 ------ 
15

7
----- explanation 1 ------ 
Example case 1: Here, $Z = 15$ maximises the function, since $F(7,12,15) = 84$. It is impossible to reach $F > 84$ with any $Z$ in the given range.

Example case 2: The smallest $Z$ which maximises $F$ is $Z = 7$, and the value of $F$ for this $Z$ is $28$.
"""

def find_optimal_z(X, Y, L, R):
    """
    Finds the smallest value of Z in the range [L, R] that maximizes the function F(X, Y, Z).

    Parameters:
    X (int): The first non-negative integer.
    Y (int): The second non-negative integer.
    L (int): The lower bound of the range for Z.
    R (int): The upper bound of the range for Z.

    Returns:
    int: The smallest value of Z in the range [L, R] that maximizes F(X, Y, Z).
    """
    
    def func(x, y, z):
        return (x & z) * (y & z)
    
    def recursion(lo, ans):
        if lo & (lo - 1) == 0:
            x = lo | ans
            return x
        else:
            y = recursion(lo & (lo - 1), ans)
            if y >= L:
                return y
            return lo | ans
    
    q = X | Y
    if X == 0 or Y == 0:
        return L
    elif q >= L and q <= R:
        return q
    else:
        maxx = func(X, Y, R)
        ans = R
        z = R
        while z:
            temp = z - 1
            if temp < L:
                break
            if func(X, Y, temp) >= maxx:
                maxx = func(X, Y, temp)
                ans = temp
            z = z & (z - 1)
        if func(X, Y, L) >= maxx:
            maxx = func(X, Y, L)
            ans = L
        s = ans & q
        if s >= L:
            return s
        else:
            x = recursion(L, s)
            return x