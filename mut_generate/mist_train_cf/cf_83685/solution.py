"""
QUESTION:
Implement a function `sequenceReconstruction(org, seqs)` where `org` and `seqs` are lists of integers. `org` is the original sequence and `seqs` is a list of sequences. The function should return a tuple of two boolean values. The first value is `True` if `org` can be uniquely reconstructed from `seqs`, `False` otherwise. The second value is `True` if the length of `org` is greater than 0, `False` otherwise. If `org` cannot be reconstructed from `seqs` or if `org` is empty, the function should return `False` for both values.
"""

def sequenceReconstruction(org, seqs):
    values = {k for seq in seqs for k in seq}

    # Create the graph
    graph = {x: [] for x in values}
    in_edge_count = {x: 0 for x in values}

    # Generate the graph
    for seq in seqs:
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:  
                return False, False
            graph[seq[i]].append(seq[i+1])
            in_edge_count[seq[i+1]] += 1

    # Check if this is the same set of values
    if set(org) != values:
        return False, False

    # Do the topological sort and matching
    for node in org:
        if in_edge_count[node] != 0:
            return False, False

        if len(graph[node]) > 0:
            if len(graph[node]) > 1:   
                return False, False
            in_edge_count[graph[node][0]] -= 1
            del graph[node]

    return len(graph) == 0, len(org) > 0