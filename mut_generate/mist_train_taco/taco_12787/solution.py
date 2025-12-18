"""
QUESTION:
Given a number N, identify the pattern from  the given Examples and print the Output.
 
Example 1:
Input:
N = 4
Output:
ABCD
E$$F
G$$H
IJKL
Example 2:
Input:
N = 6
Output:
ABCDEF
G$$$$H
I$$$$J
K$$$$L
M$$$$N
OPQRST
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findThePattern() which takes an Integer N as input and returns a vector of strings where each line represents lines of the pattern. For example, if N = 4, the vector v = {"ABCD", "E$$F", "G$$H", "IJKL"}.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N <= 6
"""

def generate_pattern(N: int) -> list[str]:
    ch = 0
    pattern = []
    for i in range(N):
        line = ''
        for j in range(N):
            if i == 0 or j == 0 or i == N - 1 or j == N - 1:
                line += chr(ch + 65)
                ch += 1
            else:
                line += '$'
        pattern.append(line)
    return pattern