"""
QUESTION:
The chef is trying to decode some pattern problems, Chef wants your help to code it. Chef has one number K(odd) to form a new pattern. Help the chef to code this pattern problem.

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
3
5
7

-----Sample Output:-----
1
111
111
111
11111
11 11
1 1 1
11 11
11111
1111111
11   11
1 1 1 1
1  1  1
1 1 1 1
11   11
1111111

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(K):
    pattern = []
    for i in range(K):
        line = []
        for j in range(K):
            if i == 0 or i == K - 1 or j == 0 or j == K - 1 or i == j or i + j == K - 1:
                line.append('1')
            else:
                line.append(' ')
        pattern.append(''.join(line))
    return pattern