"""
QUESTION:
Write a function `ratio_nonterminal_total` that calculates the ratio of nonterminal nodes to total nodes in a complete K-ary tree of depth N. The function should take two parameters, `K` and `N`, where `K` is the number of children each node has and `N` is the depth of the tree. The function should return the calculated ratio.
"""

def ratio_nonterminal_total(K, N):
    total_nodes = (K**(N+1) - 1) / (K - 1)
    terminal_nodes = K**N
    nonterminal_nodes = total_nodes - terminal_nodes
    ratio = nonterminal_nodes / total_nodes
    return ratio