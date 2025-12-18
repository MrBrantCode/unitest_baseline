"""
QUESTION:
You are given a string S consisting of 0 and 1.
Find the maximum integer K not greater than |S| such that we can turn all the characters of S into 0 by repeating the following operation some number of times.
 - Choose a contiguous segment [l,r] in S whose length is at least K (that is, r-l+1\geq K must be satisfied). For each integer i such that l\leq i\leq r, do the following: if S_i is 0, replace it with 1; if S_i is 1, replace it with 0.

-----Constraints-----
 - 1\leq |S|\leq 10^5
 - S_i(1\leq i\leq N) is either 0 or 1.

-----Input-----
Input is given from Standard Input in the following format:
S

-----Output-----
Print the maximum integer K such that we can turn all the characters of S into 0 by repeating the operation some number of times.

-----Sample Input-----
010

-----Sample Output-----
2

We can turn all the characters of S into 0 by the following operations:
 - Perform the operation on the segment S[1,3] with length 3. S is now 101.
 - Perform the operation on the segment S[1,2] with length 2. S is now 011.
 - Perform the operation on the segment S[2,3] with length 2. S is now 000.
"""

def find_max_k_to_flip_all_zeros(S: str) -> int:
    cums = [0] * (len(S) + 1)
    for i in range(len(S)):
        cums[i + 1] = cums[i] + int(S[i])
    
    ans = len(S)
    l = 0
    r = len(S) - 1
    
    while l <= r:
        x = cums[r + 1] - cums[l]
        if x == r - l + 1 or x == 0:
            break
        ans -= 1
        l += 1
        r -= 1
    
    return ans