"""
QUESTION:
M items are to be delivered in a circle of size N. Find the position where the M-th item will be delivered if we start from a given position K. Note that items are distributed at adjacent positions starting from K.
 
Example 1:
Input:
N = 5, M = 2, K = 1
Output:
2
Explanation:
If we start from 1st position, the
2nd item will land at the 2nd position.
Example 2:
Input:
N = 5, M = 8, K = 2
Output:
4
Explanation:
If we start from 2nd position, the
8th item will land at the 4th position.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findPosition() which takes 3 Integers N,M and K as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N,M,K <= 10^{5}
"""

def find_delivery_position(N: int, M: int, K: int) -> int:
    nums_to_beg = N - (K - 1)
    if M <= nums_to_beg:
        return K - 1 + M
    else:
        answer = (M - nums_to_beg) % N
        if answer == 0:
            return N
        else:
            return answer