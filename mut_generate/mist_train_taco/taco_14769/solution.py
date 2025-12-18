"""
QUESTION:
The chef is trying to decode some pattern problems, Chef wants your help to code it. Chef has one number K to form a new pattern. Help the chef to code this pattern problem.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, one integer $K$. 

-----Output:-----
For each test case, output as the pattern.

-----Constraints-----
- $1 \leq T \leq 100$
- $1 \leq K \leq 100$

-----Sample Input:-----
4
1
2
3
4

-----Sample Output:-----
0
01
10
012
101
210
0123
1012
2101
3210

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(K: int) -> list[str]:
    if K == 1:
        return ['0']
    
    pattern = []
    s = [str(i) for i in range(K)]
    pattern.append(''.join(s))
    
    p = 1
    for _ in range(K - 1):
        s.pop(K - 1)
        s = [str(p)] + s
        pattern.append(''.join(s))
        p += 1
    
    return pattern