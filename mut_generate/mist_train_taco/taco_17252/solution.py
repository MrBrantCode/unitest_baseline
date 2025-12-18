"""
QUESTION:
Calculate the power of an army of numbers from 1 to $N$, both included.

-----Input:-----
- First line will contain a single integer $N$.

-----Output:-----
For each testcase, output in a single line containing the answer.

-----Constraints-----
- $1 \leq N \leq 5000$

-----Sample Input:-----
24

-----Sample Output:-----
5
"""

def calculate_army_power(N: int) -> int:
    plist = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]
    power = 1
    
    for i in range(2, N + 1):
        pdiv = []
        count = 0
        
        for p in plist:
            if i >= p and i % p == 0:
                pdiv.append(p)
        
        for pd in pdiv:
            if i % (pd ** 2) == 0:
                count += 1
        
        if count == len(pdiv) and count != 0:
            power += 1
    
    return power