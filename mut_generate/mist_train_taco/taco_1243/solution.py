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
1 01 
11 001 
1 01 11 
001 101 011 
111 0001 1001 
1 01 11 001 
101 011 111 0001 
1001 0101 1101 0011 
1011 0111 1111 00001 

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(T, K_list):
    results = []
    for K in K_list:
        pattern = []
        cnt = 1
        for i in range(K):
            s = ''
            for j in range(K):
                s += str(bin(cnt))[2:][::-1] + ' '
                cnt += 1
            pattern.append(s.strip())
        results.append('\n'.join(pattern))
    return results