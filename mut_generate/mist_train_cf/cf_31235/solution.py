"""
QUESTION:
Implement the `match_leaves` function, which takes two parameters: 
- `leafpred`: A function that takes a leaf object as input and returns a value based on some predicate evaluation.
- `leaves`: A list of leaf objects to be evaluated using the `leafpred` function.

The function should return a dictionary mapping leaf objects to their corresponding predicate evaluation results, utilizing a cache to store and retrieve results of previous evaluations to avoid redundant computations.
"""

def match_leaves(leafpred, leaves):
    leafcache = {}  
    result_mapping = {}  

    for leaf in leaves:
        if leaf in leafcache:  
            result_mapping[leaf] = leafcache[leaf]  
        else:
            result = leafpred(leaf)  
            leafcache[leaf] = result  
            result_mapping[leaf] = result  

    return result_mapping