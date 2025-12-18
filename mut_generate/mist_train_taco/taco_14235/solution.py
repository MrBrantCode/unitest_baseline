"""
QUESTION:
You have an empty sequence, and you will be given $N$ queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

Function Description  

Complete the getMax function in the editor below.   

getMax has the following parameters: 

- string operations[n]: operations as strings   

Returns 

- int[]: the answers to each type 3 query   

Input Format

The first line of input contains an integer, $n$. The next $n$ lines each contain an above mentioned query.   

Constraints

Constraints 

$1\leq n\leq10^5$ 

$1\leq x\leq10^9$ 

$1\leq type\leq3$ 

All queries are valid.  

Sample Input
STDIN   Function
-----   --------
10      operations[] size n = 10
1 97    operations = ['1 97', '2', '1 20', ....]
2
1 20
2
1 26
1 20
2
3
1 91
3

Sample Output
26
91
"""

def process_stack_operations(operations):
    stack = []
    max_elements = []
    current_max = float('-inf')
    
    for operation in operations:
        entries = operation.split()
        if entries[0] == '1':
            value = int(entries[1])
            stack.append(value)
            if value > current_max:
                current_max = value
        elif entries[0] == '2':
            if stack:
                popped_value = stack.pop()
                if popped_value == current_max:
                    if stack:
                        current_max = max(stack)
                    else:
                        current_max = float('-inf')
        elif entries[0] == '3':
            if stack:
                max_elements.append(current_max)
    
    return max_elements