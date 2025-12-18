"""
QUESTION:
Find the number of unique words consisting of lowercase alphabets only of length N that can be formed with at-most K contiguous vowels. 
Example 1:
Input:
N = 2
K = 0
Output:
441
Explanation:
Total of 441 unique words are possible
of length 2 that will have K( =0) vowels
together, e.g. "bc", "cd", "df", etc are
valid words while "ab" (with 1 vowel) is
not a valid word.
Example 2:
Input:
N = 1
K = 1
Output:
26
Explanation:
All the english alphabets including
vowels and consonants; as atmost K( =1)
vowel can be taken.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function kvowelwords() which takes an Integer N, an intege K and returns the total number of words of size N with atmost K vowels. As the answer maybe to large please return answer modulo 1000000007.
Expected Time Complexity: O(N*K)
Expected Auxiliary Space: O(N*K)
Constraints:
1 ≤ N ≤ 1000
0 ≤ K ≤ N
"""

def kvowelwords(N, K):
    NV = 5  # Number of vowels
    NC = 26 - NV  # Number of consonants
    MOD = 1000000007
    
    # Initialize memoization table
    memo = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
    
    # Base case: when N = 0, there is exactly one empty word
    memo[0][0] = 1
    
    # Fill the memoization table
    for i in range(1, N + 1):
        for j in range(K + 1):
            if j == 0:
                # If no vowels are allowed, we can only use consonants
                memo[i][j] = NC * sum(memo[i - 1]) % MOD
            else:
                # If j vowels are allowed, we can use either a consonant or a vowel
                memo[i][j] = (NV * memo[i - 1][j - 1] + NC * memo[i - 1][j]) % MOD
    
    # The result is the sum of all possibilities for words of length N
    return sum(memo[N]) % MOD