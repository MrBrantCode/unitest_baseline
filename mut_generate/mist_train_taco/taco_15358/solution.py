"""
QUESTION:
The chef is trying to solve some pattern problems, Chef wants your help to code it. Chef has one number K to form a new pattern. Help the chef to code this pattern problem.

-----Input:-----
-First-line will contain $T$, the number of test cases. Then the test cases follow.
-Each test case contains a single line of input, one integer $K$.

-----Output:-----
For each test case, output as the pattern.

-----Constraints-----
- $1 \leq T \leq 26$
- $1 \leq K \leq 26$

-----Sample Input:-----
2
2
4

-----Sample Output:-----
A
12
A
12
ABC
1234

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(K: int) -> list[str]:
    pattern = []
    for i in range(1, K + 1):
        line = ' ' * (K - i)
        if i % 2 == 1:
            line += ''.join(chr(65 + j) for j in range(i))
        else:
            line += ''.join(str(j + 1) for j in range(i))
        pattern.append(line)
    return pattern