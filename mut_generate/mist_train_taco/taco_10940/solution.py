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
*
*
**
*
**
***
*
**
* *
****
*
**
* *
*  *
*****

-----EXPLANATION:-----
No need, else pattern can be decode easily.
"""

def generate_patterns(T, test_cases):
    """
    Generates patterns for each test case based on the given integer K.

    Parameters:
    - T (int): The number of test cases.
    - test_cases (list of int): A list of integers K for which patterns need to be generated.

    Returns:
    - list of str: A list where each element is the pattern for the corresponding K.
    """
    def generate_pattern(K):
        pattern = []
        for i in range(K - 1):
            if i == 0:
                pattern.append('*')
            else:
                pattern.append('*' + ' ' * (i - 1) + '*')
        pattern.append('*' * K)
        return '\n'.join(pattern)
    
    patterns = []
    for K in test_cases:
        patterns.append(generate_pattern(K))
    
    return patterns