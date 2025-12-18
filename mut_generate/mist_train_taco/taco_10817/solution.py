"""
QUESTION:
Given two integer array A and B of size N each.
A sum combination is made by adding one element from array A and another element of array B.
Return the maximum K valid distinct sum combinations from all the possible sum combinations.
Note : Output array must be sorted in non-increasing order.
Example 1:
Input:
N = 2
C = 2
A [ ] = {3, 2}
B [ ] = {1, 4}
Output: {7, 6}
Explanation: 
7 -> (A : 3) + (B : 4)
6 -> (A : 2) + (B : 4)
Example 2:
Input:
N = 4
C = 3
A [ ] = {1, 4, 2, 3}
B [ ] = {2, 5, 1, 6}
Output: {10, 9, 9}
Explanation: 
10 -> (A : 4) + (B : 6)
9 -> (A : 4) + (B : 5)
9 -> (A : 3) + (B : 6)
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxCombinations() which takes the interger N,integer K and two integer arrays A [ ] and B [ ] as parameters and returns the maximum K valid distinct sum combinations .
Expected Time Complexity: O(Klog(N))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤  10^{5}
1 ≤ K ≤  N
1 ≤ A [ i ] , B [ i ] ≤ 1000
"""

def max_combinations(N, K, A, B):
    import heapq
    
    # Sort arrays A and B
    A.sort()
    B.sort()
    
    # Initialize a priority queue (min-heap)
    pq = []
    heapq.heapify(pq)
    
    # Push the largest possible sum combination into the heap
    heapq.heappush(pq, (-(A[N - 1] + B[N - 1]), (N - 1, N - 1)))
    
    # Set to keep track of visited indices
    visited = set()
    visited.add((N - 1, N - 1))
    
    result = []
    
    for _ in range(K):
        # Pop the smallest element from the heap (which is actually the largest due to negation)
        current_sum, (i, j) = heapq.heappop(pq)
        result.append(-current_sum)
        
        # Generate the next possible sums
        if i > 0:
            next_sum = A[i - 1] + B[j]
            next_indices = (i - 1, j)
            if next_indices not in visited:
                heapq.heappush(pq, (-next_sum, next_indices))
                visited.add(next_indices)
        
        if j > 0:
            next_sum = A[i] + B[j - 1]
            next_indices = (i, j - 1)
            if next_indices not in visited:
                heapq.heappush(pq, (-next_sum, next_indices))
                visited.add(next_indices)
    
    return result