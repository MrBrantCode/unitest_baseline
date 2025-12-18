"""
QUESTION:
Find the count of all possible strings of size n.Each character of the string is either ‘R’, ‘B’ or ‘G’. In the final string there needs to be at least r number of ‘R’, at least b number of ‘B’ and at least g number of ‘G’ (such that r + g + b <= n). 
Example 1:
Input: n = 4, r = 1, g = 1, b = 1
Output: 36 
Explanation: No. of 'R' >= 1, 
No. of ‘G’ >= 1, No. of ‘B’ >= 1 
and (No. of ‘R’) + (No. of ‘B’) 
+ (No. of ‘G’) = n then 
following cases are possible: 
1. RBGR and its 12 permutation 
2. RBGB and its 12 permutation 
3. RBGG and its 12 permutation 
Hence answer is 36.
Example 2:
Input: n = 4, r = 2, g = 0, b = 1
Output: 22
Explanation: No. of 'R' >= 2,
No. of ‘G’ >= 0, No. of ‘B’ >= 1
and (No. of ‘R’) + (No. of ‘B’)
+ (No. of ‘G’) <= n then 
following cases are possible:
1. RRBR and its 4 permutation
2. RRBG and its 12 permutation
3. RRBB and its 6 permutation
Hence answer is 22.
Your Task:  
You dont need to read input or print anything. Complete the function possibleStrings() which takes n, r, g, b as input parameter and returns the count of number of all possible strings..
Expected Time Complexity: O(n^{2})
Expected Auxiliary Space: O(n)
Constraints:
1<= n <=20
1<= r+b+g <=n
"""

def count_possible_strings(n, r, g, b):
    k1 = n - (r + b + g)

    def fact(a):
        f = 1
        if a == 1 or a == 0:
            return 1
        for i in range(1, a + 1):
            f = f * i
        return f
    
    s = 0
    for i in range(k1 + 1):
        k = k1 - i
        for j in range(k + 1):
            llm = k - j
            l1 = fact(n) // (fact(r + i) * fact(b + j) * fact(g + llm))
            s = s + l1
    return s