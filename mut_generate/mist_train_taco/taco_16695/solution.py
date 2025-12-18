"""
QUESTION:
Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.
Example 1:
Input:
N = 4
X[] = 5,15,1,3
Output:
5
10
5
4
Explanation:Flow in stream : 5, 15, 1, 3 
5 goes to stream --> median 5 (5) 
15 goes to stream --> median 10 (5,15) 
1 goes to stream --> median 5 (5,15,1) 
3 goes to stream --> median 4 (5,15,1 3) 
 
Example 2:
Input:
N = 3
X[] = 5,10,15
Output:
5
7.5
10
Explanation:Flow in stream : 5, 10, 15
5 goes to stream --> median 5 (5) 
10 goes to stream --> median 7.5 (5,10) 
15 goes to stream --> median 10 (5,10,15) 
Your Task:
You are required to complete the class Solution. 
It should have 2 data members to represent 2 heaps. 
It should have the following member functions:
	insertHeap() which takes x as input and inserts it into the heap, the function should then call balanceHeaps() to balance the new heap.
	balanceHeaps() does not take any arguments. It is supposed to balance the two heaps.
	getMedian() does not take any arguments. It should return the current median of the stream.
Expected Time Complexity : O(nlogn)
Expected Auxilliary Space : O(n)
 
Constraints:
1 <= N <= 10^{6}
1 <= x <= 10^{6}
"""

import heapq

def find_median_of_stream(nums):
    def balance_heaps():
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

    def get_median():
        if len(max_heap) == len(min_heap):
            return (-max_heap[0] + min_heap[0]) / 2
        else:
            return -max_heap[0]

    def insert_heaps(num):
        if not max_heap or num < -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        balance_heaps()

    max_heap = []
    min_heap = []
    medians = []

    for num in nums:
        insert_heaps(num)
        medians.append(get_median())

    return medians