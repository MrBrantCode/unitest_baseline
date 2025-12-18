"""
QUESTION:
Create a function ` QuietestAndRicher` that takes three parameters: `richer`, `quiet`, and `intelligent`, where `richer` is a list of lists, `quiet` and `intelligent` are lists. The function should return a list `answer` where `answer[x] = y` if `y` is the least quiet entity among all entities who are verified to possess equal or greater wealth than entity `x` and have an intelligence level greater than or equal to `intelligent[x]`. 

Restrictions: 
1. `1 <= len(quiet) = N <= 500`
2. `0 <= quiet[i] < N`, all `quiet[i]` are unique.
3. `0 <= intelligent[i] < N`, all `intelligent[i]` are unique.
4. `0 <= len(richer) <= N * (N-1) / 2`
5. `0 <= richer[i][j] < N`
6. `richer[i][0] != richer[i][1]`
7. `richer[i]`'s are all unique.
8. The observations in `richer` are all logically consistent.
"""

def QuietestAndRicher(richer, quiet, intelligent):
    graph = [[] for _ in range(len(quiet))]
    for u, v in richer:
        graph[v].append(u)
        
    sorted_entities = sorted(range(len(intelligent)), key=lambda x: intelligent[x], reverse=True)
    answer = list(range(len(quiet)))
    
    for entity in sorted_entities:
        for richer_entity in graph[entity]:
            if quiet[answer[richer_entity]] > quiet[answer[entity]]:
                answer[richer_entity] = answer[entity]
                
    return answer