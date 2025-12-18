"""
QUESTION:
Square Subsequences

A string is called a square string if it can be obtained by concatenating two copies of the same string. For example, "abab", "aa" are square strings, while "aaa", "abba" are not. Given a string, how many (non-empty) subsequences of the string are square strings? A subsequence of a string can be obtained by deleting zero or more characters from it, and maintaining the relative order of the remaining characters.

Input Format

The first line contains the number of test cases, $T$. 

$T$ test cases follow. Each case contains a string, $S$.

Output Format

Output $T$ lines, one for each test case, containing the required answer modulo 1000000007.

Constraints: 

$1\leq T\leq20$ 

$S$ will have at most $200$ lowercase characters ('a' - 'z').

Sample Input

3 

aaa 

abab 

baaba

Sample Output

3 

3 

6

Explanation

For the first case, there are 3 subsequences of length 2, all of which are square strings. 

For the second case, the subsequences "abab", "aa", "bb" are square strings. 

Similarly, for the third case, "bb", "baba" (twice), and "aa" (3 of them) are the square subsequences.
"""

def count_square_subsequences(S: str) -> int:
    """
    Counts the number of non-empty subsequences of the string S that are square strings.
    
    A square string is a string that can be obtained by concatenating two copies of the same string.
    
    Parameters:
    S (str): The input string for which square subsequences need to be counted.
    
    Returns:
    int: The number of square subsequences modulo 1000000007.
    """
    def count_subsequences(s, t):
        m = len(s)
        n = len(t)
        T = [[0 for _ in range(n)] for _ in range(m)]
        T[0][0] = 1 if s[0] == t[0] else 0
        for i in range(1, n):
            T[0][i] = T[0][i - 1] + (1 if s[0] == t[i] else 0)
            T[0][i] %= 1000000007
        for i in range(1, m):
            T[i][0] = T[i - 1][0]
            T[i][0] %= 1000000007
        for i in range(1, m):
            for j in range(1, n):
                T[i][j] = T[i - 1][j] + T[i][j - 1] + (0 if s[i] == t[j] else -T[i - 1][j - 1])
                T[i][j] %= 1000000007
        return T[m - 1][n - 1]
    
    m = len(S)
    R = 0
    for i in range(1, m):
        R += count_subsequences(S[i:], S[:i])
        R %= 1000000007
    return R