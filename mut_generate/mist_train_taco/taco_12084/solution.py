"""
QUESTION:
Given an integer N. Your task is to identify the pattern from the Examples and print the pattern.
 
Example 1: 
Input:
N = 4
Output:
4444444 
4333334 
4322234 
4321234 
4322234 
4333334 
4444444
Example 2: 
Input:
N = 3
Output:
33333 
32223 
32123 
32223 
33333
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function interestingPattern() which takes an Integer N as input and returns a vector of strings where each line representins each line of the pattern. For example, if N = 3, you have to return a vector v = {"33333", "32223", "32123", "32223", "33333"}.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N < 10
"""

def generate_interesting_pattern(N):
    if N == 1:
        return ["1"]
    
    pattern = []
    
    # Generate the top half of the pattern
    for i in range(N, 0, -1):
        s = '' + str(N)
        k = N
        for j in range(0, N - i):
            k = k - 1
            s = s + str(k)
        s = s + (i - 1) * str(k)
        r = s[::-1]
        s = s + r[1:]
        pattern.append(s)
    
    # Generate the bottom half of the pattern
    pattern = pattern + pattern[::-1][1:]
    
    return pattern