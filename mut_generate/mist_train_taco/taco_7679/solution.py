"""
QUESTION:
Chef stumbled upon B black nodes and W white nodes and now wants to construct a tree using them.

Chef is bamboozled by the total number of trees that can be constructed using these nodes. To reduce this count, Chef considered only those trees which have at least one diameter that has alternating colors i.e. a black node is followed by a white node and a white node is followed by a black node.

Help Chef in finding out the tree with the minimum possible diameter among all the trees that satisfies the above condition. If no tree satisfies the above conditions, print -1. If multiple trees satisfies the above condition, print any.

------ Input Format ------ 

- The first line contains a single integer T - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space separated integers B, W representing the number of black and white nodes respectively.

------ Output Format ------ 

- If a tree can be constructed that fulfils all the requirements then
- In the first line, output a string of length B + W in which the i^{th} character (1-based indexing) is either W or B denoting the colour of the i^{th} node as black or white respectively.
- In the following B + W - 1 lines, output two integers U and V denoting an edge between U^{th} and V^{th} node.
- If no tree fulfils the requirements print -1 in a single line. 

------ Constraints ------ 

$1 ≤ T ≤ 100$
$0 ≤ B, W ≤ 1000$
$1 ≤ B + W ≤ 1000$

----- Sample Input 1 ------ 
3
1 1
0 2
1 2

----- Sample Output 1 ------ 
WB
2 1
-1
WBW
1 2
2 3

----- explanation 1 ------ 
Test case $1$: The tree has only one path between the nodes $1$ and $2$ which is the diameter and also alternating in color. The checker will handle multiple possible answers so you can also swap the colors of the node to achieve the same result. 

Test case $2$: There is only one tree possible and its diameter would consist of all white nodes only. Therefore there is no tree which satisfies the given conditions.
"""

def construct_alternating_tree(B, W):
    """
    Constructs a tree with alternating colors of nodes and returns the tree structure or -1 if no valid tree can be constructed.

    Parameters:
    B (int): Number of black nodes.
    W (int): Number of white nodes.

    Returns:
    dict or int: A dictionary containing the tree structure with keys 'nodes' and 'edges', or -1 if no valid tree can be constructed.
    """
    N = W + B
    if N == 1:
        if W:
            return {'nodes': 'W', 'edges': []}
        else:
            return {'nodes': 'B', 'edges': []}
    elif N == 2:
        if W == 0 or B == 0:
            return -1
        return {'nodes': 'WB', 'edges': [(1, 2)]}
    else:
        if W == 0 or B == 0:
            return -1
        if B > 1:
            st = 'BWB'
            B -= 2
            W -= 1
        else:
            st = 'WBW'
            W -= 2
            B -= 1
        st = st + 'B' * B + 'W' * W
        edges = [(1, 2), (2, 3)]
        for end in range(4, 4 + B):
            edges.append((2, end))
        for end in range(4 + B, 4 + W + B):
            edges.append((2, end))
        return {'nodes': st, 'edges': edges}