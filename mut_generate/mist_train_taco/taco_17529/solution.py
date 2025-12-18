"""
QUESTION:
Given an array arr[] of size N, enqueue the elements of the array into a queue and then dequeue them.
Example 1:
Input:
N = 5 
arr[] = 1 2 3 4 5 
Output: 
1 2 3 4 5
Example 2:
Input:
N = 7
arr[] = 1 6 43 1 2 0 5
Output:
1 6 43 1 2 0 5
Your Task:
You don't need to read any input. Your task is to complete the functions push() and _pop(). The function push() takes the array and its size as the input parameters and returns the queue formed, and the function _pop(), takes the queue as the input parameter and prints the elements of the queue.
 
Expected time complexity: O(n)
Expected space complexity: O(n)
 
Constraints:
1 <= A_{i} <= 10^{7}
"""

def process_array_to_queue(arr, n):
    # Step 1: Enqueue elements into a queue
    queue = []
    for i in range(n):
        queue.append(arr[i])
    
    # Step 2: Dequeue elements and store them in a list
    dequeued_elements = []
    while queue:
        dequeued_elements.append(queue.pop(0))
    
    # Step 3: Return the queue and the dequeued elements
    return queue, dequeued_elements