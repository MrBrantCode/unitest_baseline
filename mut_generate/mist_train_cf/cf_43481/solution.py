"""
QUESTION:
Implement a function `max_val(a, k)` that selects k elements from array `a` such that the sum of the product of their indices and corresponding elements is maximized. The function should take two parameters: `a`, an array of integers, and `k`, an integer representing the number of elements to select. The function should return the maximum sum of products of indices and corresponding elements. Assume that array indices are 0-based and start from the right (i.e., the last element has an index equal to the length of the array minus one).
"""

import heapq

def max_val(a, k): 
    if len(a) == 0 or k<=0: 
        return 0
    
    result = 0 
    max_heap = [] 
    for i in range(len(a)): 
        heapq.heappush(max_heap, (-a[i]*i, a[i], i))  
    
    while k>0: 
        val, element, index = heapq.heappop(max_heap)
        result += (-1)*val  
        index -= 1
        val = element*index if index>=0 else 0
                
        heapq.heappush(max_heap, (-val, element, index)) 
        k -= 1
    
    return result