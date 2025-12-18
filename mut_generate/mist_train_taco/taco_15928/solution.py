"""
QUESTION:
Mitya has a rooted tree with n vertices indexed from 1 to n, where the root has index 1. Each vertex v initially had an integer number a_v ≥ 0 written on it. For every vertex v Mitya has computed s_v: the sum of all values written on the vertices on the path from vertex v to the root, as well as h_v — the depth of vertex v, which denotes the number of vertices on the path from vertex v to the root. Clearly, s_1=a_1 and h_1=1.

Then Mitya erased all numbers a_v, and by accident he also erased all values s_v for vertices with even depth (vertices with even h_v). Your task is to restore the values a_v for every vertex, or determine that Mitya made a mistake. In case there are multiple ways to restore the values, you're required to find one which minimizes the total sum of values a_v for all vertices in the tree.

Input

The first line contains one integer n — the number of vertices in the tree (2 ≤ n ≤ 10^5). The following line contains integers p_2, p_3, ... p_n, where p_i stands for the parent of vertex with index i in the tree (1 ≤ p_i < i). The last line contains integer values s_1, s_2, ..., s_n (-1 ≤ s_v ≤ 10^9), where erased values are replaced by -1.

Output

Output one integer — the minimum total sum of all values a_v in the original tree, or -1 if such tree does not exist.

Examples

Input


5
1 1 1 1
1 -1 -1 -1 -1


Output


1


Input


5
1 2 3 1
1 -1 2 -1 -1


Output


2


Input


3
1 2
2 -1 1


Output


-1
"""

def calculate_minimum_total_sum(n, parents, sums):
    pc_list = [[0, []] for _ in range(n)]
    a_list = [0] * n
    a_list[0] = sums[0]
    
    for vertex, parent in enumerate(parents):
        pc_list[vertex + 1][0] = parent - 1
        pc_list[parent - 1][1].append(vertex + 1)
    
    stack = [(0, 0)]
    invalid = False
    
    while stack and (not invalid):
        cur_vertex, child_num = stack.pop()
        parent = pc_list[cur_vertex][0]
        cur_list = pc_list[cur_vertex][1]
        
        if not cur_list and sums[cur_vertex] == -1:
            a_list[cur_vertex] = 0
        elif sums[cur_vertex] == -1 and child_num == 0:
            min_sum = min([sums[child] for child in cur_list])
            if min_sum < sums[parent]:
                invalid = True
                break
            else:
                a_list[cur_vertex] = min_sum - sums[parent]
        elif sums[cur_vertex] != -1 and cur_vertex != 0 and (child_num == 0):
            grandparent = pc_list[parent][0]
            a_list[cur_vertex] = sums[cur_vertex] - a_list[parent]
            a_list[cur_vertex] += -sums[grandparent]
        
        if child_num < len(cur_list):
            stack.append((cur_vertex, child_num + 1))
            stack.append((cur_list[child_num], 0))
    
    if invalid:
        return -1
    else:
        return sum(a_list)