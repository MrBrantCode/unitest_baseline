"""
QUESTION:
Given a string, S find the rank of the string amongst all its permutations sorted lexicographically.The rank can be big. So print it modulo 1000003. 
Note: Return 0 if the characters are repeated in the string.
Example 1:
Input: S = "abc"
Output: 1
Explaination: It is the smallest 
lexicographically string of the permutation.
Example 2:
Input: S = "acb"
Output: 2
Explaination: This is the second smallest
lexicographically string of the permutation.
Your Task:
You do not need to read input or print anything. Your task is to complete the function rank() which takes string S as input parameter and returns the rank modulo 1000003 of the string.
Expected Time Complexity: O(|S|^{2})
Expected Auxiliary Space: O(|S|)
Constraints:
1 ≤ |S| ≤ 15
"""

from collections import defaultdict
import math

def calculate_lexicographic_rank(S: str) -> int:
    hmap = defaultdict(int)
    for c in S:
        hmap[c] += 1
    for count in hmap.values():
        if count > 1:
            return 0
    
    st = list(S)
    size = len(st)
    qt = sorted(st)
    rank = 1
    
    while st and qt:
        n = st.pop(0)
        size -= 1
        inx = qt.index(n)
        rank += inx * math.factorial(size)
        qt.remove(n)
    
    return rank % 1000003