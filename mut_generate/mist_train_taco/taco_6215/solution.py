"""
QUESTION:
Shaun was given $N$ pairs of parenthesis ( )  by his teacher who gave him a difficult task.The task consists of two steps. First,Shaun should colour all $N$ pairs of parenthesis each with different color but opening and closing bracket of a particular pair should be of same colour. Then,Shaun should report to his teacher the number of ways he can arrange all $2*N$ brackets such that sequence form is valid. Teacher defined valid sequence by these rules:
- Any left parenthesis '(' must have a corresponding right parenthesis ')'.
- Any right parenthesis ')' must have a corresponding left parenthesis '('.
- Left parenthesis '(' must go before the corresponding right parenthesis ')'. 
Note: Shaun could match opening and closing brackets of different colours. 
Since number of ways can be large, Shaun would report the answer as modulo 1000000007 ($10^9 + 7$).

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input, one integer $N$. 

-----Output:-----
For each testcase, output in a single line answer given by Shaun to his teacher modulo 1000000007.

-----Constraints-----
- $1 \leq T \leq 100000$
- $1 \leq N \leq 100000$

-----Sample Input:-----
3
1
2
3

-----Sample Output:-----
1
6
90

-----EXPLANATION:-----
Here numbers from $1$ to $N$ have been used to denote parenthesis.A unique number corresponds to a unique pair of parenthesis.
-In the first test case , you can use only one color to color the parenthesis  you could arrange it only in one way i.e, 1 1
-In the second test case  you can use two colors and the possible ways of arranging it are
1 1 2 2
1 2 2 1
1 2 1 2
2 2 1 1
2 1 1 2
2 1 2 1
"""

def count_valid_arrangements(T: int, N: list[int]) -> list[int]:
    """
    Calculate the number of valid arrangements of N pairs of parentheses for each test case, modulo 1000000007.

    Parameters:
    - T (int): Number of test cases.
    - N (list[int]): List of integers where each integer represents the number of pairs of parentheses for each test case.

    Returns:
    - list[int]: List of integers where each integer is the result for the corresponding test case, modulo 1000000007.
    """
    mod = 1000000007
    maxn = 100000 + 5
    
    # Precompute factorials up to maxn
    fac = [1, 1]
    for i in range(2, maxn):
        x = fac[-1] * i % mod
        fac.append(x)
    
    # Precompute pre values up to maxn
    pre = [1]
    for i in range(2, maxn):
        x = 2 * i - 1
        x = pre[-1] * x % mod
        pre.append(x)
    
    results = []
    for n in N:
        x = fac[n]
        y = pre[n - 1]
        results.append(x * y % mod)
    
    return results