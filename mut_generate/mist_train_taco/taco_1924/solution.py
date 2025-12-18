"""
QUESTION:
For a set $S$ of integers, perform a sequence of the following operations. Note that multiple elements can have equivalent values in $S$.

* insert($x$): Insert $x$ to $S$ and report the number of elements in $S$ after the operation.
* find($x$): Report the number of $x$ in $S$.
* delete($x$): Delete all $x$ from $S$.
* dump($L$, $R$): Print elements $x$ in $S$ such that $L \leq x \leq R$.

Constraints

* $1 \leq q \leq 200,000$
* $0 \leq x \leq 1,000,000,000$
* The total number of elements printed by dump operations does not exceed $1,000,000$
* The sum of numbers printed by find operations does not exceed $2,000,000$

Input

The input is given in the following format.


$q$
$query_1$
$query_2$
:
$query_q$


Each query $query_i$ is given by


0 $x$


or


1 $x$


or


2 $x$


or


3 $L$ $R$


where the first digits 0, 1, 2 and 3 represent insert, find, delete and dump operations respectively.

Output

For each insert operation, print the number of elements in $S$.
For each find operation, print the number of specified elements in $S$.
For each dump operation, print the corresponding elements in ascending order. Print an element in a line.

Example

Input

10
0 1
0 1
0 2
0 3
2 2
1 1
1 2
1 3
0 4
3 1 4


Output

1
2
3
4
2
0
1
4
1
1
3
4
"""

import bisect
import collections

def process_queries(queries):
    values = collections.defaultdict(int)
    element_count = 0
    results = []
    
    for query in queries:
        com, *para = query
        if com == 0:  # insert(x)
            values[para[0]] += 1
            element_count += 1
            results.append(element_count)
        elif com == 1:  # find(x)
            results.append(values[para[0]])
        elif com == 2:  # delete(x)
            element_count -= values[para[0]]
            values[para[0]] = 0
        elif com == 3:  # dump(L, R)
            L, R = para
            if L == R:
                for _ in range(values[L]):
                    results.append(L)
            elif abs(L - R) < 10:
                for i in range(L, R + 1):
                    for _ in range(values[i]):
                        results.append(i)
            else:
                key_list = [k for k, v in values.items() if v != 0]
                key_list = sorted(key_list)
                lb = bisect.bisect_left(key_list, L)
                rb = bisect.bisect_right(key_list, R)
                for s in key_list[lb:rb]:
                    for _ in range(values[s]):
                        results.append(s)
    
    return results