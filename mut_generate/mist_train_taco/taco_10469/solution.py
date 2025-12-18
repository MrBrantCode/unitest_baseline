"""
QUESTION:
The chef is trying to solve some pattern problems, Chef wants your help to code it. Chef has one number K to form a new pattern. Help the chef to code this pattern problem.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, one integer $K$. 

-----Output:-----
For each test case, output as the pattern.

-----Constraints-----
- $1 \leq T \leq 100$
- $1 \leq K \leq 100$

-----Sample Input:-----
5
1
2
3
4
5

-----Sample Output:-----
1
1
32
1
32
654
1
32
654
10987
1
32
654
10987
1514131211

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(K: int) -> list[str]:
    pattern = []
    for i in range(K):
        line = ''
        for j in range(i + 1):
            line += str(int((i + 1) * (i + 2) / 2) - j)
        pattern.append(line)
    return pattern