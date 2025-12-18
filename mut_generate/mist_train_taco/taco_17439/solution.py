"""
QUESTION:
You have a string $s$ consisting of $n$ characters. Each character is either 0 or 1.

You can perform operations on the string. Each operation consists of two steps:  select an integer $i$ from $1$ to the length of the string $s$, then delete the character $s_i$ (the string length gets reduced by $1$, the indices of characters to the right of the deleted one also get reduced by $1$);  if the string $s$ is not empty, delete the maximum length prefix consisting of the same characters (the indices of the remaining characters and the string length get reduced by the length of the deleted prefix). 

Note that both steps are mandatory in each operation, and their order cannot be changed.

For example, if you have a string $s =$ 111010, the first operation can be one of the following:  select $i = 1$: we'll get 111010 $\rightarrow$ 11010 $\rightarrow$ 010;  select $i = 2$: we'll get 111010 $\rightarrow$ 11010 $\rightarrow$ 010;  select $i = 3$: we'll get 111010 $\rightarrow$ 11010 $\rightarrow$ 010;  select $i = 4$: we'll get 111010 $\rightarrow$ 11110 $\rightarrow$ 0;  select $i = 5$: we'll get 111010 $\rightarrow$ 11100 $\rightarrow$ 00;  select $i = 6$: we'll get 111010 $\rightarrow$ 11101 $\rightarrow$ 01. 

You finish performing operations when the string $s$ becomes empty. What is the maximum number of operations you can perform?


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 1000$) — the number of test cases.

The first line of each test case contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the length of the string $s$.

The second line contains string $s$ of $n$ characters. Each character is either 0 or 1.

It's guaranteed that the total sum of $n$ over test cases doesn't exceed $2 \cdot 10^5$.


-----Output-----

For each test case, print a single integer — the maximum number of operations you can perform.


-----Example-----
Input
5
6
111010
1
0
1
1
2
11
6
101010

Output
3
1
1
1
3



-----Note-----

In the first test case, you can, for example, select $i = 2$ and get string 010 after the first operation. After that, you can select $i = 3$ and get string 1. Finally, you can only select $i = 1$ and get empty string.
"""

def max_operations(s: str) -> int:
    n = len(s)
    if n < 3:
        return 1
    
    a = []
    b = []
    c = 1
    j = 0
    
    for i in range(1, n):
        if s[i] == s[i - 1]:
            c += 1
        else:
            a.append(c)
            if c > 1:
                b.append(j)
            c = 1
            j += 1
    
    a.append(c)
    if c > 1:
        b.append(j)
    
    la = len(a)
    lb = len(b)
    
    if lb == 0:
        return (la + 1) // 2
    
    ia = ib = r = 0
    while ia < la:
        r += 1
        if a[ia] == 1:
            a[b[ib]] -= 1
            if a[b[ib]] == 1:
                ib += 1
                if ib >= lb:
                    r += (la - ia) // 2
                    break
        else:
            ib += 1
            if ib >= lb:
                r += (la - ia) // 2
                break
        ia += 1
    
    return r