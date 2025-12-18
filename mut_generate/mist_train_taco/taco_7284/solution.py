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
2
2
4

-----Sample Output:-----
2
21
210
21
2
4
43
432
4321
43210
4321
432
43
4

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_pattern(T, K_list):
    """
    Generates a pattern for each value of K in K_list.

    Parameters:
    - T (int): The number of test cases.
    - K_list (list of int): A list of integers where each integer represents the value of K for each test case.

    Returns:
    - list of str: A list of strings where each string represents the pattern for the corresponding K value.
    """
    if T != len(K_list):
        raise ValueError("The number of test cases T must match the length of K_list.")
    
    patterns = []
    
    for K in K_list:
        pattern = []
        
        # Generate the first part of the pattern
        for i in range(K + 1):
            line = ''.join(str(K - j) for j in range(i + 1))
            pattern.append(line)
        
        # Generate the second part of the pattern
        for l in range(K):
            line = ''.join(str(K - j) for j in range(K - l))
            pattern.append(line)
        
        patterns.append('\n'.join(pattern))
    
    return patterns