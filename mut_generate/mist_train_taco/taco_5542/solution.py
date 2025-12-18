"""
QUESTION:
For a dynamic list $L$ of integers, perform a sequence of the following operations. $L$ has a special element called END at the end of the list and an element of $L$ is indicated by a cursor.

* insert($x$): Insert $x$ before the element indicated by the cursor. After this operation, the cursor points the inserted element.
* move($d$): Move the cursor to the end by $d$, if $d$ is positive. Move the cursor to the front by $d$, if $d$ is negative.
* erase(): Delete the element indicated by the cursor. After this operation, the cursor points the element next to the deleted element. In case there is no such element, the cursor should point END.



In the initial state, $L$ is empty and the cursor points END.

Constraints

* $1 \leq q \leq 500,000$
* The cursor indicates an element of $L$ or END during the operations
* Erase operation will not given when the cursor points END
* $-1,000,000,000 \leq x \leq 1,000,000,000$
* Moving distance of the cursor ($\sum{|d|}$) does not exceed 1,000,000
* $L$ is not empty after performing all operations

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


1 $d$


or


2


where the first digits 0, 1 and 2 represent insert, move and erase operations respectively.

Output

Print all elements of the list in order after performing given operations. Print an element in a line.

Example

Input

5
0 1
0 2
0 3
1 1
2


Output

3
1
"""

def process_operations(operations):
    A = [0] * 1500000
    A[0] = 'end'
    cursor = 0
    head = [0] * 1500000
    head_len = 0

    def insert(x):
        nonlocal cursor
        cursor += 1
        A[cursor] = x

    def move(d):
        nonlocal cursor, head, head_len
        if d >= 0:
            head[head_len - 1 + d + 1:head_len - 1 + 1:-1] = A[cursor - d + 1:cursor + 1]
        else:
            A[cursor + 1:cursor + 1 + -d] = head[head_len - 1 + 1:head_len - -d - 1 + 1:-1]
        cursor -= d
        head_len += d

    def erase():
        nonlocal cursor
        cursor -= 1

    for op in operations:
        if op[0] == 0:
            insert(op[1])
        elif op[0] == 1:
            move(op[1])
        elif op[0] == 2:
            erase()

    A[cursor + 1:cursor + 1 + head_len] = head[head_len - 1 + 1:-1 + 1:-1]
    length = cursor + head_len
    result = [A[i] for i in range(1, length + 1)[::-1] if A[i] != 'end']
    return result