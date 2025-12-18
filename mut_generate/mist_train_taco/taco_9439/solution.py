"""
QUESTION:
You are given N elements, you can remove any two elements from the list, note their sum, and add the sum to the list. Repeat these steps while there is more than a single element in the list. The task is to minimize the sum of these chosen sums.
 
Example 1:
Input:
N = 4
arr[] = {1, 4, 7, 10}
Output:
39
Explanation:
Choose 1 and 4, Sum = 1 + 4 = 5.
arr[] = {5, 7, 10} 
Choose 5 and 7, Sum = 5 + (5 + 7) = 17.
arr[] = {12, 10} 
Choose 12 and 10, Sum = 17 + (12 + 10) = 39.
arr[] = {22}
 
Example 2:
Input:
N = 5
arr[] = {1, 3, 7, 5, 6}
Output:
48
 
Your Task:
You don't need to read input or print anything. The task is to complete the function minimizeSum() which takes N as size of arr array and a arr array. Your task is to minimize the sum of these chosen sums and return it.
 
Expected Time Complexity: O(N * log(N))
Expected Auxiliary Space: O(N)
 
Constraints:
1 <= N, arr[i] <= 10^{5}
"""

import heapq

def minimize_sum(N, arr):
    minheap = []
    total_sum = 0
    
    # Push all elements into the min-heap
    for i in range(N):
        heapq.heappush(minheap, arr[i])
    
    # Continue until there is only one element left in the heap
    while len(minheap) > 1:
        # Pop the two smallest elements
        temp1 = heapq.heappop(minheap)
        temp2 = heapq.heappop(minheap)
        
        # Calculate their sum
        summ = temp1 + temp2
        
        # Add the sum to the total sum
        total_sum += summ
        
        # Push the sum back into the heap
        heapq.heappush(minheap, summ)
    
    return total_sum