"""
QUESTION:
In a finite directed acyclic graph (DAG) G = (V, E) where |E| > 0, which statements must inevitably hold true? 
I. The graph G embodies a vertex bereft of any incoming edge.
II. The graph G incorporates a vertex devoid of any outgoing edge.
III. The graph G entails an isolated vertex, signifying a vertex sans an incoming edge or an outgoing edge.
"""

def identify_sources_and_sinks(G):
    sources = [node for node, in_degree in G.in_degree() if in_degree == 0]
    sinks = [node for node, out_degree in G.out_degree() if out_degree == 0]
    return sources, sinks