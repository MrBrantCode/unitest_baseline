"""
QUESTION:
You are given a permutation of 1,2,...,N: p_1,p_2,...,p_N. Determine if the state where p_i=i for every i can be reached by performing the following operation any number of times:
 - Choose three elements p_{i-1},p_{i},p_{i+1} (2\leq i\leq N-1) such that p_{i-1}>p_{i}>p_{i+1} and reverse the order of these three.

-----Constraints-----
 - 3 \leq N \leq 3 × 10^5
 - p_1,p_2,...,p_N is a permutation of 1,2,...,N.

-----Input-----
Input is given from Standard Input in the following format:
N
p_1
:
p_N

-----Output-----
If the state where p_i=i for every i can be reached by performing the operation, print Yes; otherwise, print No.

-----Sample Input-----
5
5
2
1
4
3

-----Sample Output-----
Yes

The state where p_i=i for every i can be reached as follows:
 - Reverse the order of p_1,p_2,p_3. The sequence p becomes 1,2,5,4,3.
 - Reverse the order of p_3,p_4,p_5. The sequence p becomes 1,2,3,4,5.
"""

def can_reach_sorted_state(N, P):
    # Add a dummy element at the beginning to make indexing easier
    P = [0] + P
    
    intervals = []
    left = 0
    right = -1
    
    for i, p in enumerate(P):
        if right < p:
            right = p
        if i == right:
            intervals.append((left, right))
            left = i + 1
            right = -1
    
    def check(L, R):
        if L == R:
            return True
        
        to_left = []
        fixed = []
        to_right = []
        
        for i, p in enumerate(P[L:R + 1], L):
            if i > p:
                to_left.append(p)
            elif i == p:
                fixed.append(p)
            else:
                to_right.append(p)
        
        if fixed != list(range(L + 1, R + 1, 2)):
            return False
        
        if any(x > y for x, y in zip(to_left, to_left[1:])):
            return False
        
        if any(x > y for x, y in zip(to_right, to_right[1:])):
            return False
        
        return True
    
    answer = 'Yes' if all(check(L, R) for L, R in intervals) else 'No'
    return answer