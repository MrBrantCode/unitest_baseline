"""
QUESTION:
Larry has been given a permutation of a sequence of natural numbers incrementing from $\mbox{1}$ as an array.  He must determine whether the array can be sorted using the following operation any number of times:  

Choose any $3$ consecutive indices and rotate their elements in such a way that $ABC\:\to\text{}BCA\:\to\text{}CAB\:\to\text{}ABC$. 

For example, if $A=\{1,6,5,2,4,3\}$:

A		rotate 
[1,6,5,2,4,3]	[6,5,2]
[1,5,2,6,4,3]	[5,2,6]
[1,2,6,5,4,3]	[5,4,3]
[1,2,6,3,5,4]	[6,3,5]
[1,2,3,5,6,4]	[5,6,4]
[1,2,3,4,5,6]

YES

On a new line for each test case, print YES if $\mbox{A}$ can be fully sorted.  Otherwise, print NO.  

Function Description  

Complete the larrysArray function in the editor below.  It must return a string, either YES or NO.  

larrysArray has the following parameter(s):  

A: an array of integers  

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of test cases.   

The next $\boldsymbol{\boldsymbol{t}}$ pairs of lines are as follows:  

The first line contains an integer $n$, the length of $\mbox{A}$.
The next line contains $n$ space-separated integers $A[i]$.

Constraints

$1\leq t\leq10$
$3\leq n\leq1000$
$1\leq A[i]\leq n$
$A_{sorted}=$ integers that increment by $\mbox{1}$ from $\mbox{1}$ to $n$

Output Format

For each test case, print YES if $\mbox{A}$ can be fully sorted.  Otherwise, print NO.

Sample Input
3
3
3 1 2
4
1 3 4 2
5
1 2 3 5 4

Sample Output
YES
YES
NO

Explanation

In the explanation below, the subscript of $\mbox{A}$ denotes the number of operations performed.

Test Case 0: 

$A_0=\{3,1,2\}\to\text{rotate}(3,1,2)\to A_1=\{1,2,3\}$ 

$\mbox{A}$ is now sorted, so we print $\textbf{YES}$ on a new line.

Test Case 1: 

$A_0=\{1,3,4,2\}\to\text{rotate}(3,4,2)\to A_1=\{1,4,2,3\}$. 

$A_1=\{1,4,2,3\}\to\text{rotate}(4,2,3)\to A_2=\{1,2,3,4\}$. 

$\mbox{A}$ is now sorted, so we print $\textbf{YES}$ on a new line.

Test Case 2:

No sequence of rotations will result in a sorted $\mbox{A}$. Thus, we print $\boldsymbol{\textbf{NO}}$ on a new line.
"""

def can_be_sorted_with_rotations(A):
    sorted_list = sorted(A)
    list_len = len(A)
    
    for i in range(list_len - 2):
        if A[i] == sorted_list[i]:
            continue
        
        my_ind = A.index(sorted_list[i])
        while my_ind > i:
            if my_ind == list_len - 1:
                # Rotate the last three elements
                A[my_ind - 2], A[my_ind - 1], A[my_ind] = A[my_ind - 1], A[my_ind], A[my_ind - 2]
            else:
                # Rotate the current three elements
                A[my_ind - 1], A[my_ind], A[my_ind + 1] = A[my_ind], A[my_ind + 1], A[my_ind - 1]
            my_ind -= 1
    
    if A[-1] == sorted_list[-1]:
        return "YES"
    else:
        return "NO"