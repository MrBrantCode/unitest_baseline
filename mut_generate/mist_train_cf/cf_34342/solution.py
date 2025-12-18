"""
QUESTION:
Write a function `determine_relevant_linked_timepoints(timepoints, linked_timepoints, target_timepoint)` that takes in a list of unique timepoint identifiers `timepoints`, a list of linked timepoint pairs `linked_timepoints`, and a target timepoint `target_timepoint`. The function should return a list of timepoints that are directly or indirectly linked to the target timepoint, including the target timepoint itself. The relationships between timepoints are transitive and do not form cycles.
"""

from typing import List, Tuple

def entrance(timepoints: List[str], linked_timepoints: List[Tuple[str, str]], target_timepoint: str) -> List[str]:
    graph = {tp: [] for tp in timepoints}
    for tp1, tp2 in linked_timepoints:
        graph[tp1].append(tp2)
        graph[tp2].append(tp1)

    relevant_linked_timepoints = set()

    def dfs(current_tp):
        relevant_linked_timepoints.add(current_tp)
        for linked_tp in graph[current_tp]:
            if linked_tp not in relevant_linked_timepoints:
                dfs(linked_tp)

    dfs(target_timepoint)
    return list(relevant_linked_timepoints)