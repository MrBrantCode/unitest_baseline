"""
QUESTION:
The Monk learned about priority queues recently and asked his teacher for an interesting problem. So his teacher came up with a simple problem. He now has an integer array A. For each index i, he wants to find the product of the largest, second largest and the third largest integer in the range [1,i].
Note: Two numbers can be the same value-wise but they should be distinct index-wise.

Input:
The first line contains an integer N, denoting the number of elements in the array A.
The next line contains N space separated integers, each denoting the ith integer of the array A.

Output:
Print the answer for each index in each line. If there is no second largest or third largest number in the array A upto that index, then print "-1", without the quotes.

Constraints:
1 ≤ N ≤ 100000
0 ≤ A[i] ≤ 1000000

SAMPLE INPUT
5
1 2 3 4 5

SAMPLE OUTPUT
-1
-1
6
24
60

Explanation

There are 5 integers 1,2,3,4 and 5.
For the first two indexes, since the number of elements is less than 3, so -1 is printed.
For the third index, the top 3 numbers are 3,2 and 1 whose product is 6.
For the fourth index, the top 3 numbers are 4,3, and 2 whose product is 24.
For the fifth index, the top 3 numbers are 5,4 and 3 whose product is 60.
"""

from heapq import heappush, heappop

def find_product_of_top_three(arr):
    n = len(arr)
    result = []
    heap = []
    
    for i in range(n):
        heappush(heap, -arr[i])
        
        if len(heap) < 3:
            result.append(-1)
            continue
        
        first = heappop(heap)
        second = heappop(heap)
        third = heappop(heap)
        
        result.append(-1 * first * second * third)
        
        heappush(heap, first)
        heappush(heap, second)
        heappush(heap, third)
    
    return result