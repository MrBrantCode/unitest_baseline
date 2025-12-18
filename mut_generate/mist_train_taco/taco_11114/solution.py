"""
QUESTION:
Queue is a container of elements that are inserted and deleted according to FIFO (First In First Out).

For $n$ queues $Q_i$ ($i = 0, 1, ..., n-1$), perform a sequence of the following operations.

* enqueue($t$, $x$): Insert an integer $x$ to $Q_t$.
* front($t$): Report the value which should be deleted next from $Q_t$. If $Q_t$ is empty, do nothing.
* dequeue($t$): Delete an element from $Q_t$. If $Q_t$ is empty, do nothing.



In the initial state, all queues are empty.

Constraints

* $1 \leq n \leq 1,000$
* $1 \leq q \leq 200,000$
* $-1,000,000,000 \leq x \leq 1,000,000,000$

Input

The input is given in the following format.


$n \; q$
$query_1$
$query_2$
:
$query_q$


Each query $query_i$ is given by


0 $t$ $x$


or


1 $t$


or


2 $t$


where the first digits 0, 1 and 2 represent enqueue, front and dequeue operations respectively.

Output

For each front operation, print an integer in a line.

Example

Input

3 9
0 0 1
0 0 2
0 0 3
0 2 4
0 2 5
1 0
1 2
2 0
1 0


Output

1
4
2
"""

from collections import deque

def process_queue_operations(n, q, queries):
    qs = [deque() for _ in range(n)]
    results = []
    
    for op in queries:
        t = op[1]
        que = qs[t]
        
        if op[0] == 0:  # enqueue operation
            que.append(op[2])
        elif op[0] == 1:  # front operation
            if len(que) > 0:
                x = que.popleft()
                results.append(x)
                que.appendleft(x)
        elif op[0] == 2:  # dequeue operation
            if len(que) > 0:
                que.popleft()
    
    return results