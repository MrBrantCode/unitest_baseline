"""
QUESTION:
Write a function `calculateAttributes(G)` that takes a grammar G as input, where G is a tuple containing four elements: N (set of non-terminal symbols), T (set of terminal symbols), S (start symbol), and P (set of production rules). The function should return the set A, which is the union of the sets of synthesized and inherited attributes for each non-terminal symbol in N. The function should not take any other inputs and should not use any external variables.
"""

def calculateAttributes(G):
    N, T, S, P = G
    attributes = {}
    
    for X in N:
        synthesized = set()
        inherited = set()
        
        # Calculate synthesized attributes based on production rules
        # Add logic here to compute synthesized attributes for non-terminal X
        # Update synthesized set
        
        # Calculate inherited attributes based on production rules
        # Add logic here to compute inherited attributes for non-terminal X
        # Update inherited set
        
        attributes[X] = {'synthesized': synthesized, 'inherited': inherited}
    
    A = set()
    for X in N:
        A = A.union(attributes[X]['synthesized']).union(attributes[X]['inherited'])
    
    return A