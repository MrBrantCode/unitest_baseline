"""
QUESTION:
Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.
Only following standard operations are allowed on queue.
	enqueue(x) : Add an item x to rear of queue
	dequeue() : Remove an item from front of queue
	size() : Returns number of elements in queue.
	front() : Finds front item.
	Note: The above operations represent the general processings. In-built functions of the respective languages can be used to solve the problem.
Example 1:
Input:
5 3
1 2 3 4 5
Output: 
3 2 1 4 5
Explanation: 
After reversing the given
input from the 3rd position the resultant
output will be 3 2 1 4 5.
Example 2:
Input:
4 4
4 3 2 1
Output: 
1 2 3 4
Explanation: 
After reversing the given
input from the 4th position the resultant
output will be 1 2 3 4.
Your Task:
Complete the provided function modifyQueue that takes queue and k as parameters and returns a modified queue. The printing is done automatically by the driver code.
Expected Time Complexity : O(N)
Expected Auxiliary Space : O(K)
Constraints:
1 <= N <= 1000
1 <= K <= N
"""

def reverse_first_k_elements(queue, k):
    if k > len(queue):
        raise ValueError("k should be less than or equal to the size of the queue")
    
    # Step 1: Extract the first k elements and reverse them
    l = []
    for i in range(k):
        l.append(queue.pop(0))
    l.reverse()
    
    # Step 2: Append the reversed elements back to the queue
    for element in l:
        queue.append(element)
    
    # Step 3: Append the remaining elements to the queue
    for i in range(len(queue) - k):
        queue.append(queue.pop(0))
    
    return queue