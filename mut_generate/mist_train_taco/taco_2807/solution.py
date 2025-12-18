"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

Chef cooks nice receipes in the cafeteria of his company. The cafe contains N boxes with food enumerated from 1 to N and are placed in a circle in clocwise order (boxes 1 and N are adjacent). Each box has unlimited amount of food with a tastyness level of A_{i}. Chef invented a definition of a magic box!
Chef picks a box i and stays in front of it. 
Now Chef eats food from box i and skips next A_{i} boxes.
Now Chef is staying at some other (probably even the same!) box and repeats. 
Box i is a magic box if at some point of such game started from box i, Chef will find himself staying in front of it again. 

When Chef came home, Chef's dog Tommy asked him about how many magic boxes were in the cafe? Help Chef to in finding that!

------ Input ------ 

The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N denoting the number of boxes.
The second line contains N space-separated integers A_{1}, A_{2}, ..., A_{N} denoting the tastyness levels of each box.

------ Output ------ 

For each test case, output a single line containing number of magical boxes.

------ Constraints ------ 

$1 ≤ sum of all N over all the test cases in a single test file ≤ 10^{6}$
$0 ≤ A_{i} ≤ 10^{9}$

------ Subtasks ------ 

$Subtask #1 (30 points): 1 ≤ sum of all N over all the test cases ≤ 10^{4}; 1 ≤ N ≤ 1000$

$Subtask #2 (70 points): 1 ≤ sum of all N over all the test cases ≤ 10^{6}; 1 ≤ N ≤ 10^{5}$

----- Sample Input 1 ------ 
3
4
1 1 1 1
4
3 0 0 0
4
0 0 0 2
----- Sample Output 1 ------ 
4
1
2
----- explanation 1 ------ 
Example case 1.
Here are Chef's paths if he starting from each the box:

1->3->1
2->4->2
3->1->3
4->2->4

As you see, all 4 boxes are magical.

Example case 2.
Here are Chef's paths if he starts from each box appropriately:

1->1
2->3->4->1->1
3->4->1->1
4->1->1

AS you see, only box 1 is magical.
"""

from collections import defaultdict

def count_magic_boxes(n, tastyness_levels):
    def dfs1(u):
        visited[u] = True
        v = (u + tastyness_levels[u] + 1) % n
        if not visited[v]:
            dfs1(v)
        order.append(u)

    def dfs2(u):
        visited[u] = True
        for adjacent in transpose[u]:
            if not visited[adjacent]:
                dfs2(adjacent)
        scc.append(u)

    transpose = defaultdict(list)
    for index, value in enumerate(tastyness_levels):
        transpose[(index + value + 1) % n].append(index)
    
    ans = 0
    visited = [False] * n
    order = []
    
    for i in range(n):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * n
    for i in range(n):
        node = order[n - 1 - i]
        scc = []
        if not visited[node]:
            dfs2(node)
            if len(scc) == 1 and scc[0] != (scc[0] + tastyness_levels[scc[0]] + 1) % n:
                continue
            ans += len(scc)
    
    return ans