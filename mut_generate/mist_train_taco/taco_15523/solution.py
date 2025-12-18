"""
QUESTION:
Let's assume that we have a pair of numbers (a, b). We can get a new pair (a + b, b) or (a, a + b) from the given pair in a single step.

Let the initial pair of numbers be (1,1). Your task is to find number k, that is, the least number of steps needed to transform (1,1) into the pair where at least one number equals n.

Input

The input contains the only integer n (1 ≤ n ≤ 106).

Output

Print the only integer k.

Examples

Input

5


Output

3


Input

1


Output

0

Note

The pair (1,1) can be transformed into a pair containing 5 in three moves: (1,1)  →  (1,2)  →  (3,2)  →  (5,2).
"""

def find_min_steps_to_reach_n(n):
    if n == 1:
        return 0
    
    res = 1000000
    
    for other in range(n - 1, 0, -1):
        pair = [n, other]
        temp = 0
        
        while (pair[0] > 1 or pair[1] > 1) and (pair[0] > 0 and pair[1] > 0):
            pair.sort()
            multiples = (pair[1] - 1) // pair[0]
            if multiples == 0:
                break
            pair[1] -= pair[0] * multiples
            temp += multiples
            if temp > res:
                break
        
        if pair[0] == 1 and pair[1] == 1:
            res = min(res, temp)
    
    return res