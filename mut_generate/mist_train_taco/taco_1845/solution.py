"""
QUESTION:
In Doraland, people have unique Identity Numbers called D-id. Doraemon owns the most popular gadget shop in Doraland. Since his gadgets are in high demand and he has only K gadgets left he has decided to sell his gadgets to his most frequent customers only. N customers visit his shop and D-id of each customer is given in an array array[ ]. In case two or more people have visited his shop the same number of time he gives priority to the customer with higher D-id. Find the D-ids of people he sells his K gadgets to.
Example 1:
Input:
N = 6
array[] = {1, 1, 1, 2, 2, 3}
K = 2
Output: 
1 2
Explanation: 
Customers with D-id 1 and 2 are most 
frequent.
Example 2:
Input:
N = 8
array[] = {1, 1, 2, 2, 3, 3, 3, 4}
K = 2
Output: 
3 2
Explanation: People with D-id 1 and 2 have 
visited shop 2 times Therefore, in this 
case, the answer includes the D-id 2 as 2 > 1.
Your Task:
You don't need to read input or print anything. Complete the function TopK() which takes array[ ] and integer K as input parameters and returns an array containing D-id of customers he has decided to sell his gadgets to.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ D-id ≤ 10^{4}
"""

import heapq
from collections import defaultdict

def top_k_customers(array, k):
    # Step 1: Count the frequency of each D-id
    frequency_map = defaultdict(int)
    for d_id in array:
        frequency_map[d_id] += 1
    
    # Step 2: Create a max-heap based on frequency and D-id
    max_heap = []
    for d_id, freq in frequency_map.items():
        heapq.heappush(max_heap, (-freq, -d_id))
    
    # Step 3: Extract the top k D-ids from the max-heap
    top_k = []
    while k > 0 and max_heap:
        _, neg_d_id = heapq.heappop(max_heap)
        top_k.append(-neg_d_id)
        k -= 1
    
    return top_k