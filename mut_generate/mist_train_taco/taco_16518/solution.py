"""
QUESTION:
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Example 1:
Input:
S = "abc"
Output:
1
Explanation:
The order permutations with letters 
'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
Example 2:
Input:
S = "acb"
Output:
2
Your Task:
You don't need to read input or print anything. Your task is to complete the function findRank() which takes the string S as input parameter and returns the rank of the string amongst its permutations.
It is guaranteed no characters are repeated in the string.
Expected Time Complexity: O(|S|*26)
Expected Auxiliary Space: O(|S|)
Note: |S| represents the length of string S.
Constraints:
1 ≤ |S| ≤ 18
"""

def find_rank(S: str) -> int:
    n = len(S)
    inp = []
    fact = 1
    
    # Calculate the factorial of n and populate the input list
    for i in range(n):
        inp.append(S[i])
        fact *= i + 1
    
    # Adjust factorial to (n-1)!
    fact = fact // n
    
    i = 0
    k = 1
    
    # Sort the input list to get lexicographical order
    inp = sorted(inp)
    
    for element in S:
        block = inp.index(element)
        k += block * fact
        inp.pop(block)
        
        if i != n - 1:
            fact = fact // (n - i - 1)
        
        i += 1
    
    return k