"""
QUESTION:
Given a list of regions where the first region in each list encompasses all other regions, write a function `findSmallestRegion(regions, region1, region2)` to find the smallest region that includes both `region1` and `region2`. The function takes in a 2D list `regions` and two strings `region1` and `region2`, and returns a string representing the smallest common region. Assume that the smallest region will always exist, and `region1 != region2`. The constraints are `2 <= regions.length <= 10^4` and all strings are composed of English letters and spaces, with a maximum of 20 letters.
"""

def findSmallestRegion(regions, region1, region2):
    parent = {}
    
    for r in regions: 
        for i in range(1, len(r)): 
            parent[r[i]] = r[0]

    p = set()
    
    while region1: 
        p.add(region1) 
        region1 = parent.get(region1)

    while region2 not in p: 
        if region2 in parent: 
            region2 = parent[region2]
        else:
            break
            
    return region2