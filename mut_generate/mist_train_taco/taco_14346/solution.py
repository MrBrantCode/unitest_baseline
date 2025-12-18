"""
QUESTION:
Chef played an interesting game yesterday. This game is played with two variables $X$ and $Y$; initially, $X = Y = 0$. Chef may make an arbitrary number of moves (including zero). In each move, he must perform the following process:
- Choose any positive integer $P$ such that $P \cdot P > Y$.
- Change $X$ to $P$.
- Add $P \cdot P$ to $Y$.
Unfortunately, Chef has a bad memory and he has forgotten the moves he made. He only remembers the value of $X$ after the game finished; let's denote it by $X_f$. Can you tell him the maximum possible number of moves he could have made in the game?

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $X_f$.

-----Output-----
For each test case, print a single line containing one integer — the maximum number of moves Chef could have made.

-----Constraints-----
- $1 \le T \le 10^5$
- $1 \le X_f \le 10^9$

-----Example Input-----
3
3
8
9

-----Example Output-----
3
5
6

-----Explanation-----
Example case 2: One possible sequence of values of $X$ is $0 \rightarrow 1 \rightarrow 2 \rightarrow 3 \rightarrow 5 \rightarrow 8$.
"""

def max_moves_for_final_X(T: int, X_f: list) -> list:
    """
    Calculate the maximum number of moves Chef could have made given the final value of X for each test case.

    Parameters:
    - T (int): The number of test cases.
    - X_f (list): A list of integers where each integer represents the final value of X for a test case.

    Returns:
    - list: A list of integers where each integer represents the maximum number of moves for the corresponding test case.
    """
    
    def bs(val, l):
        i = 0
        j = len(l) - 1
        ans = -1
        while i <= j:
            mid = i + (j - i) // 2
            if l[mid] <= val:
                ans = mid
                i = mid + 1
            else:
                j = mid - 1
        return ans + 1

    def bst(i, val):
        j = 100000000000
        ans = -1
        while i <= j:
            mid = i + (j - i) // 2
            if mid ** 2 > val:
                ans = mid
                j = mid - 1
            else:
                i = mid + 1
        return ans

    e = 10 ** 9
    l = [1]
    sum = 1
    while l[-1] <= e:
        x = bst(l[-1] + 1, sum)
        sum += x ** 2
        l.append(x)

    results = []
    for n in X_f:
        results.append(bs(n, l))
    
    return results