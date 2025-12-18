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
3
5
3
4

-----Sample Output:-----
1   1
2 2
3
4 4
5   5
1 1
2
3 3
1  1
22
33
4  4

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(K: int) -> list[str]:
    pattern = []
    b = 1
    
    if K % 2:
        c = K - 2
        for j in range(K // 2):
            pattern.append(' ' * j + str(b) + ' ' * c + str(b))
            b += 1
            c -= 2
        pattern.append(' ' * (K // 2) + str(b) + ' ' * (K // 2))
        b += 1
        c = 1
        for j in range(K // 2):
            pattern.append(' ' * (K // 2 - j - 1) + str(b) + ' ' * c + str(b))
            b += 1
            c += 2
    else:
        c = K - 2
        for j in range(K // 2):
            pattern.append(' ' * j + str(b) + ' ' * c + str(b))
            b += 1
            c -= 2
        c = 0
        for j in range(K // 2):
            pattern.append(' ' * (K // 2 - j - 1) + str(b) + ' ' * c + str(b))
            b += 1
            c += 2
    
    return pattern