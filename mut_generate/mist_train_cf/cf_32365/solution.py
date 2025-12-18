"""
QUESTION:
The function `generate_full_paths` should take in two parameters: a list of `Subcompartment` objects and a list of subcompartment names. The function should return a list of full paths for active subcompartments. 

The `Subcompartment` object has two attributes: `name` and `lifecycle_state`. The function should only construct the full path for subcompartments with a `lifecycle_state` of "ACTIVE". The full path should be constructed by concatenating the names of the subcompartments in the hierarchy, separated by slashes ("/"). The hierarchy of subcompartments is represented by the order of subcompartment names in the input list. 

The function should assume that the number of active subcompartments is less than or equal to the number of subcompartment names. The function should return an empty list if there are no active subcompartments.
"""

from typing import List

class Subcompartment:
    def __init__(self, name: str, lifecycle_state: str):
        self.name = name
        self.lifecycle_state = lifecycle_state

def generateFullPaths(subcompartments: List[Subcompartment], subcompartment_names: List[str]) -> List[str]:
    active_subcompartments = [subcompartment for subcompartment in subcompartments if subcompartment.lifecycle_state == "ACTIVE"]
    full_paths = []
    for i, subcompartment in enumerate(active_subcompartments):
        full_path = "/".join(subcompartment_names[:i+1]) + "/" + subcompartment.name
        full_paths.append(full_path)
    return full_paths