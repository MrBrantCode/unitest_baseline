"""
QUESTION:
The chef is trying to solve some pattern problems, Chef wants your help to code it. Chef has one number K to form new pattern. Help the chef to code this pattern problem.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input, one integer $K$. 

-----Output:-----
For each testcase, output as pattern.

-----Constraints-----
- $1 \leq T \leq 100$
- $1 \leq K \leq 100$

-----Sample Input:-----
2
2
4

-----Sample Output:-----
2
12
012
12
2

4
34
234
1234
01234
1234
234
34
4

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(K):
    c = []
    d = []
    start = 0
    
    while True:
        c = []
        for i in range(start):
            c.append(' ')
        for i in range(start, K + 1):
            c.append(str(i))
        start += 1
        d.append(c)
        if start > K:
            break
    
    e = d[1:]
    d.reverse()
    d = d + e
    
    pattern = [''.join(line).strip() for line in d]
    return pattern