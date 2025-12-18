"""
QUESTION:
Given two strings S1 and S2 of lower alphabet characters of length N1 and N2, we need to find the number of ways to insert a character in the first string S1 such that length of LCS of both strings increases by one.
Example 1:
Input:
N1 = 4
S1 = abab
N2 = 3
S2 = abc
Output:
3
Explanation:
LCS length of given two 
strings is 2. There are 3 
ways of insertion in str1,to 
increase the LCS length by 
one which are enumerated below, 
str1 = “abcab” str2 = “abc” LCS length = 3 
str1 = “abacb” str2 = “abc” LCS length = 3 
str1 = “ababc” str2 = “abc” LCS length = 3
Example 2:
Input:
N1 = 6
S1 = abcabc
N2 = 4
S2 = abcd
Output:
4
Explanation:
LCS length of given two
strings is 3. There are 4
ways of insertion in str1,to
increase the LCS length by
one which are enumerated below,
str1 = “abcdabc” str2 = “abcd” LCS length = 4
str1 = “abcadcb” str2 = “abcd” LCS length = 4
str1 = “abcabdc” str2 = “abcd” LCS length = 4
str1 = “abcabcd” str2 = “abcd” LCS length = 4
Your Task:
You don't need to read input or print anything. Your task is to complete the function waysToIncreaseLCSBy1() which take string S1 and string S2 of length N1 and N2 respectively as input parameters and returns the number of ways to insert a character in the first string S1 such that length of LCS of both strings increases by one.
Expected Time Complexity: O(N1 * N2) 
Expected Space Complexity: O(N1 * N2)
Constraints:
1<= N1, N2 <=100
S1 and S2 contains lower case English character
"""

def ways_to_increase_lcs_by_1(S1: str, S2: str) -> int:
    m = len(S1)
    n = len(S2)
    
    # Position array to store positions of each character in S2
    position = [[] for _ in range(26)]
    for i in range(1, n + 1):
        position[ord(S2[i - 1]) - 97].append(i)
    
    # Initialize LCS arrays
    lcsl = [[0] * (n + 2) for _ in range(m + 2)]
    lcsr = [[0] * (n + 2) for _ in range(m + 2)]
    
    # Fill lcsl array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                lcsl[i][j] = 1 + lcsl[i - 1][j - 1]
            else:
                lcsl[i][j] = max(lcsl[i - 1][j], lcsl[i][j - 1])
    
    # Fill lcsr array
    for i in range(m, 0, -1):
        for j in range(n, 0, -1):
            if S1[i - 1] == S2[j - 1]:
                lcsr[i][j] = 1 + lcsr[i + 1][j + 1]
            else:
                lcsr[i][j] = max(lcsr[i + 1][j], lcsr[i][j + 1])
    
    # Calculate the number of ways to increase LCS by 1
    ways = 0
    for i in range(m + 1):
        for C in range(26):
            for p in position[C]:
                if lcsl[i][p - 1] + lcsr[i + 1][p + 1] == lcsl[m][n]:
                    ways += 1
                    break
    
    return ways