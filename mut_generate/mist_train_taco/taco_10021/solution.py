"""
QUESTION:
Starting with any positive integer N, we define the Collatz sequence corresponding to N as the numbers formed by the following operations:
If N is even, N→ N/2
if N is odd,   N→ 3N+ 1
It is conjectured but not yet proven that no matter which positive integer we start with; we always end up with 1.
For example, 10 → 5  → 16  → 8  → 4  → 2  → 1. You have to give the maximum collatz sequence length among all the numbers from 1 to N(both included).
Example 1:
Input: N = 1
Output: 1
Explaination: Here N can have only one 
value 1.
Example 2:
Input: N = 3
Output: 8
Explaination: For N= 3 we need to check 
sequence length when sequence starts with 
1, 2, and 3.
when sequence starts with 1, it's : 1 
length = 1
when sequence starts with 2, it's : 2->1, 
length = 2
when sequence starts with 3, it's : 
3->10->5->16->8->4->2->1, length = 8.
Your Task:
You do not need to read input or print anything. Your task is to complete the function collatzLength()which takes N as input parameter and returns the maximum collatz sequence length.
Expected Time Complexity:O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 < N < 10^{6}
"""

def collatz_length_util(n, coll_len_map):
    if n in coll_len_map:
        return coll_len_map[n]
    if n == 1:
        coll_len_map[n] = 1
    elif n % 2 == 0:
        coll_len_map[n] = 1 + collatz_length_util(n // 2, coll_len_map)
    else:
        coll_len_map[n] = 1 + collatz_length_util(3 * n + 1, coll_len_map)
    return coll_len_map[n]

def max_collatz_sequence_length(N):
    coll_len_map = {}
    max_length = 0
    
    for i in range(1, N + 1):
        if i not in coll_len_map:
            collatz_length_util(i, coll_len_map)
        current_length = coll_len_map[i]
        if max_length < current_length:
            max_length = current_length
    
    return max_length