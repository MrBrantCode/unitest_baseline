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
1
10
10
101
101
101
1010
1010
1010
1010

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(K: int) -> list[str]:
    num = ''
    val = 1
    for i in range(K):
        num += str(val)
        if val == 1:
            val = 0
        else:
            val = 1
    
    pattern = [num] * K
    return pattern