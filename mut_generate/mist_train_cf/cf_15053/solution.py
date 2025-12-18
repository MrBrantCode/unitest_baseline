"""
QUESTION:
Create a function called `allocate_resources` that takes a list of lists as input where each inner list contains a party's name and the number of resources it needs. The function should return a list of party names in the order they should be allocated resources based on their priority and the number of available resources. The priority is determined by the order of the parties in the input list. If there are not enough resources to allocate to a party, skip that party and move on to the next one.
"""

from typing import List, Any

def allocate_resources(data: List[List[Any]]) -> List[str]:
    allocated_parties = []
    available_resources = sum([party[1] for party in data])
    
    for party in data:
        if party[1] <= available_resources:
            allocated_parties.append(party[0])
            available_resources -= party[1]
    
    return allocated_parties