"""
QUESTION:
Consider a list (list = []). You can perform the following commands:   

insert i e: Insert integer $\boldsymbol{\mathrm{~e~}}$ at position $\boldsymbol{i}$.
print: Print the list.
remove e: Delete the first occurrence of integer $\boldsymbol{\mathrm{~e~}}$.
append e: Insert integer $\boldsymbol{\mathrm{~e~}}$ at the end of the list.  
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of $n$ followed by $n$ lines of commands where each command will be of the $7$ types listed above. Iterate through each command in order and perform the corresponding operation on your list.  

Example 

$N=4$ 

$append 1$ 

$append 2$ 

$insert 3 1$ 

$print$ 

$append 1$: Append $\mbox{I}$ to the list, $arr=[1]$.  
$append 2$: Append $2$ to the list, $arr=[1,2]$.  
$insert 3 1$: Insert $3$ at index $\mbox{I}$, $arr=[1,3,2]$.  
$print$: Print the array. 

Output:

[1, 3, 2]

Input Format

The first line contains an integer, $n$, denoting the number of commands. 

Each line $\boldsymbol{i}$ of the $n$ subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

def process_list_commands(commands, initial_list=None):
    if initial_list is None:
        L = []
    else:
        L = initial_list
    
    results = []
    
    for command in commands:
        args = command.split()
        if args[0] == 'append':
            L.append(int(args[1]))
        elif args[0] == 'insert':
            L.insert(int(args[1]), int(args[2]))
        elif args[0] == 'remove':
            L.remove(int(args[1]))
        elif args[0] == 'pop':
            L.pop()
        elif args[0] == 'sort':
            L.sort()
        elif args[0] == 'reverse':
            L.reverse()
        elif args[0] == 'print':
            results.append(L[:])  # Append a copy of the current list state
    
    return results