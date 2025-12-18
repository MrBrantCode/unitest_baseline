"""
QUESTION:
Given two lists V1 and V2 of sizes n and m respectively. Return the list of elements common to both the lists and return the list in sorted order. Duplicates may be there in the output list.
Example:
Input:
n = 5
v1[] = {3, 4, 2, 2, 4}
m = 4
v2[] = {3, 2, 2, 7}
Output:
2 2 3
Explanation:
The common elements in sorted order are {2 2 3}
Your Task:
This is a function problem. You need to complete the function common_element that takes both the lists as parameters and returns a list of common elements. 
Constraints:
1 ≤ n, m ≤ 10^{5}
1 ≤ V_{i} ≤ 10^{5}
"""

def find_common_elements(v1, v2):
    res = []
    map = {}
    
    # Count occurrences of each element in v1
    for i in v1:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    
    # Sort v2 to ensure the result is in sorted order
    v2.sort()
    
    # Find common elements and add to result list
    for i in v2:
        if i in map and map[i] > 0:
            res.append(i)
            map[i] -= 1
    
    return res