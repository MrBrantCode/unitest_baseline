"""
QUESTION:
Stack is a container of elements that are inserted and deleted according to LIFO (Last In First Out).

For $n$ stack $S_i$ ($i = 0, 1, ..., n-1$), perform a sequence of the following operations.

* push($t$, $x$): Insert an integer $x$ to $S_t$.
* top($t$): Report the value which should be deleted next from $S_t$. If $S_t$ is empty, do nothing.
* pop($t$): Delete an element from $S_t$. If $S_t$ is empty, do nothing.



In the initial state, all stacks are empty.

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


where the first digits 0, 1 and 2 represent push, top and pop operations respectively.

Output

For each top operation, print an integer in a line.

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

3
5
2
"""

def process_stack_operations(n, q, queries):
    stacks = [[] for _ in range(n)]
    results = []
    
    for query in queries:
        k = query[0]
        t = query[1]
        
        if k == 0:  # push operation
            x = query[2]
            stacks[t].append(x)
        
        elif k == 1:  # top operation
            if stacks[t]:
                results.append(stacks[t][-1])
        
        elif k == 2:  # pop operation
            if stacks[t]:
                stacks[t].pop()
    
    return results