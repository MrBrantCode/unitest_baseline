"""
QUESTION:
Let N be a positive integer.
There is a numerical sequence of length 3N, a = (a_1, a_2, ..., a_{3N}).
Snuke is constructing a new sequence of length 2N, a', by removing exactly N elements from a without changing the order of the remaining elements.
Here, the score of a' is defined as follows: (the sum of the elements in the first half of a') - (the sum of the elements in the second half of a').
Find the maximum possible score of a'.

-----Constraints-----
 - 1 ≤ N ≤ 10^5
 - a_i is an integer.
 - 1 ≤ a_i ≤ 10^9

-----Partial Score-----
 - In the test set worth 300 points, N ≤ 1000.

-----Input-----
Input is given from Standard Input in the following format:
N
a_1 a_2 ... a_{3N}

-----Output-----
Print the maximum possible score of a'.

-----Sample Input-----
2
3 1 4 1 5 9

-----Sample Output-----
1

When a_2 and a_6 are removed, a' will be (3, 4, 1, 5), which has a score of (3 + 4) - (1 + 5) = 1.
"""

def max_score_after_removal(N, A):
    """
    Calculate the maximum possible score of the sequence a' after removing exactly N elements from a.

    Parameters:
    N (int): The positive integer defining the length of the sequence.
    A (list of int): The numerical sequence of length 3N.

    Returns:
    int: The maximum possible score of the new sequence a'.
    """
    from heapq import heapify, heappushpop

    # Initialize the front and back sums
    front = A[:N]
    fsum = [0] * (3 * N)
    fsum[N - 1] = sum(front)
    heapify(front)
    
    for i in range(N, 2 * N):
        fmin = heappushpop(front, A[i])
        fsum[i] = fsum[i - 1] + A[i] - fmin
    
    back = [-1 * a for a in A[2 * N:]]
    bsum = [0] * (3 * N)
    bsum[2 * N] = -1 * sum(back)
    heapify(back)
    
    for i in range(2 * N - 1, N - 1, -1):
        bmax = -1 * heappushpop(back, -1 * A[i])
        bsum[i] = bsum[i + 1] + A[i] - bmax
    
    ans = -10 ** 18
    for i in range(N - 1, 2 * N):
        ans = max(ans, fsum[i] - bsum[i + 1])
    
    return ans