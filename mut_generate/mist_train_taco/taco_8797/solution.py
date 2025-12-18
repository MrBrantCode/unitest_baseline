"""
QUESTION:
You are given three non-negative integers $X$, $Y$ and $N$. Find the number of integers $Z$ such that $0 \le Z \le N$ and $(X \oplus Z) < (Y \oplus Z)$, where $\oplus$ denotes the bitwise XOR operation.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $X$, $Y$ and $N$.

-----Output-----
For each test case, print a single line containing one integer ― the number of integers $Z$ which satisfy all conditions.

-----Constraints-----
- $1 \le T \le 1,000$
- $0 \le X, Y, N \le 2^{30} - 1$

-----Subtasks-----
Subtask #1 (5 points): $X, Y, N \le 2^6 - 1$
Subtask #2 (95 points): original constraints

-----Example Input-----
3
1 2 10
2 1 10
0 0 7

-----Example Output-----
6
5
0
"""

def count_valid_Z(X, Y, N):
    bx = list(bin(X))[2:]  # Convert X to binary and remove the '0b' prefix
    by = list(bin(Y))[2:]  # Convert Y to binary and remove the '0b' prefix
    
    lx = len(bx)
    ly = len(by)
    
    index = 0
    flag = 2
    k = -1
    
    if lx != ly:
        index = max(lx, ly)
        if (N + 1) % 2 ** index >= 2 ** (index - 1):
            k = 2 ** (index - 1)
        else:
            k = (N + 1) % 2 ** index
        
        if lx < ly:
            return int((N + 1) / 2 ** index) * 2 ** (index - 1) + k
        else:
            return N + 1 - (int((N + 1) / 2 ** index) * 2 ** (index - 1) + k)
    else:
        for j in range(lx):
            if bx[j] != by[j]:
                index = lx - j
                if bx[j] == '0':
                    flag = 0
                else:
                    flag = 1
                break
        
        if (N + 1) % 2 ** index >= 2 ** (index - 1):
            k = 2 ** (index - 1)
        else:
            k = (N + 1) % 2 ** index
        
        if flag == 2:
            return 0
        elif flag == 1:
            return N + 1 - (int((N + 1) / 2 ** index) * 2 ** (index - 1) + k)
        else:
            return int((N + 1) / 2 ** index) * 2 ** (index - 1) + k