"""
QUESTION:
The chef is trying to solve some pattern problems, Chef wants your help to code it. Chef has one number K to form a new pattern. Help the chef to code this pattern problem.

-----Input:-----
- First-line will contain $T$, the number of test cases. Then the test cases follow. 
- Each test case contains a single line of input, one integer $K$. 

-----Output:-----
For each test case, output as the pattern.

-----Constraints-----
- $1 \leq T \leq 50$
- $1 \leq K \leq 50$

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
23
1
23
456
1
23
4 5
6789
1
23
4 5
6  7
89101112

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(K: int) -> list[str]:
    if K == 1:
        return ["1"]
    
    pattern = []
    count = 1
    l = 3 * (K - 1)
    i = 0
    
    while count <= l - K:
        line = []
        for j in range(i + 1):
            if j == i:
                line.append(str(count))
                count += 1
            elif j == 0:
                line.append(str(count))
                count += 1
            else:
                line.append(' ')
        pattern.append(''.join(line))
        i += 1
    
    last_line = ''.join(str(count + j) for j in range(K))
    pattern.append(last_line)
    
    return pattern