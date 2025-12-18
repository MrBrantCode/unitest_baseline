"""
QUESTION:
After the lessons n groups of friends went outside and decided to visit Pawan to celebrate his birthday. We know that the i-th group consists of si friends (1 ≤ si ≤ 4), and they want to go to Pawan together. They decided to get there by taxi. Each car can carry at most four passengers. What minimum number of cars will the children need if all members of each group should ride in the same taxi (but one taxi can take more than one group)?

Input
The first line contains integer n (1 ≤ n ≤ 105) — the number of groups of schoolchildren. The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ si ≤ 4). The integers are separated by a space, si is the number of children in the i-th group.

Output
Print the single number — the minimum number of taxis necessary to drive all children to Pawan.

SAMPLE INPUT
5
1 2 4 3 3

SAMPLE OUTPUT
4
"""

def calculate_minimum_taxis(n, groups):
    # Calculate the total number of children
    total_children = sum(groups)
    
    # Calculate the minimum number of taxis needed
    if total_children % 4 == 0:
        min_taxis = total_children // 4
    else:
        min_taxis = total_children // 4 + 1
    
    return min_taxis