"""
QUESTION:
Create a function `analyze_external_vertices(graph)` that takes a graph as input and returns four sets of vertices based on the following criteria:
1. `extern_in_fermion_vtcs`: Vertices connected to edges of weight 1 and are also external vertices.
2. `extern_out_fermion_vtcs`: Vertices connected to edges of weight 1 and are also external vertices.
3. `extern_in_ghost_vtcs`: Vertices connected to edges of weight 3 and are also external vertices.
4. `extern_out_ghost_vtcs`: Vertices connected to edges of weight 3 and are also external vertices.

Assume the input graph has the following properties:
- The graph is represented using a data structure with `edges` and `external_vtcs_set` attributes.
- The `edges` attribute is a dictionary where each edge is a key and its corresponding value is another dictionary containing the edge's properties, including its `weight`.
- The `external_vtcs_set` attribute is a set of external vertices in the graph.
"""

def analyze_external_vertices(graph):
    extern_in_fermion_vtcs = set()
    extern_out_fermion_vtcs = set()
    extern_in_ghost_vtcs = set()
    extern_out_ghost_vtcs = set()

    for edge in graph.edges:
        weight = graph.edges[edge]['weight']
        if weight == 1:
            if edge[0] in graph.external_vtcs_set:
                extern_in_fermion_vtcs.add(edge[0])
            if edge[1] in graph.external_vtcs_set:
                extern_out_fermion_vtcs.add(edge[1])
        elif weight == 3:
            if edge[0] in graph.external_vtcs_set:
                extern_in_ghost_vtcs.add(edge[0])
            if edge[1] in graph.external_vtcs_set:
                extern_out_ghost_vtcs.add(edge[1])

    return extern_in_fermion_vtcs, extern_out_fermion_vtcs, extern_in_ghost_vtcs, extern_out_ghost_vtcs