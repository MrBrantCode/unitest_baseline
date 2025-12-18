"""
QUESTION:
Implement a Queue using Linked List. 
A Query Q is of 2 Types
(i) 1 x   (a query of this type means  pushing 'x' into the queue)
(ii) 2     (a query of this type means to pop an element from the queue and print the poped element)
Example 1:
Input:
Q = 5
Queries = 1 2 1 3 2 1 4 2
Output: 2 3
Explanation: n the first testcase
1 2 the queue will be {2}
1 3 the queue will be {2 3}
2   poped element will be 2 the
    queue will be {3}
1 4 the queue will be {3 4}
2   poped element will be 3.
Example 2:
Input:
Q = 4
Queries = 1 2 2 2 1 3 
Output: 2 -1
Explanation: In the second testcase 
1 2 the queue will be {2}
2   poped element will be {2} then
    the queue will be empty. 
2   the queue is empty and hence -1
1 3 the queue will be {3}.
Your Task:
Complete the function push() which takes an integer as input parameter and pop() which will remove and return an element(-1 if queue is empty).
Expected Time Complexity: O(1).
Expected Auxiliary Space: O(1).
Constraints:
1 <= Q <= 100
1 <= x <= 100
"""

def process_queue_queries(queries):
    """
    Process a series of queue operations and return the results of pop operations.

    Parameters:
    queries (list of tuples): A list of queries where each query is a tuple.
        - (1, x) indicates a push operation with value x.
        - (2,) indicates a pop operation.

    Returns:
    list of int: A list of results from the pop operations. If a pop operation is performed on an empty queue, it returns -1.
    """
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class MyQueue:
        def __init__(self):
            self.front = None
            self.rear = None

        def push(self, item):
            node = Node(item)
            if self.front is None:
                self.front = self.rear = node
            else:
                self.rear.next = node
                self.rear = node

        def pop(self):
            if self.front is None:
                return -1
            value = self.front.data
            if self.front == self.rear:
                self.front = self.rear = None
            else:
                self.front = self.front.next
            return value

    queue = MyQueue()
    results = []

    for query in queries:
        if query[0] == 1:
            queue.push(query[1])
        elif query[0] == 2:
            results.append(queue.pop())

    return results