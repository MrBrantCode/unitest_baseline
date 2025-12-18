"""
QUESTION:
Do you know a story about the three musketeers? Anyway, you will learn about its origins now.

Richelimakieu is a cardinal in the city of Bearis. He is tired of dealing with crime by himself. He needs three brave warriors to help him to fight against bad guys.

There are n warriors. Richelimakieu wants to choose three of them to become musketeers but it's not that easy. The most important condition is that musketeers must know each other to cooperate efficiently. And they shouldn't be too well known because they could be betrayed by old friends. For each musketeer his recognition is the number of warriors he knows, excluding other two musketeers.

Help Richelimakieu! Find if it is possible to choose three musketeers knowing each other, and what is minimum possible sum of their recognitions.


-----Input-----

The first line contains two space-separated integers, n and m (3 ≤ n ≤ 4000, 0 ≤ m ≤ 4000) — respectively number of warriors and number of pairs of warriors knowing each other.

i-th of the following m lines contains two space-separated integers a_{i} and b_{i} (1 ≤ a_{i}, b_{i} ≤ n, a_{i} ≠ b_{i}). Warriors a_{i} and b_{i} know each other. Each pair of warriors will be listed at most once.


-----Output-----

If Richelimakieu can choose three musketeers, print the minimum possible sum of their recognitions. Otherwise, print "-1" (without the quotes).


-----Examples-----
Input
5 6
1 2
1 3
2 3
2 4
3 4
4 5

Output
2

Input
7 4
2 1
3 6
5 1
1 7

Output
-1



-----Note-----

In the first sample Richelimakieu should choose a triple 1, 2, 3. The first musketeer doesn't know anyone except other two musketeers so his recognition is 0. The second musketeer has recognition 1 because he knows warrior number 4. The third musketeer also has recognition 1 because he knows warrior 4. Sum of recognitions is 0 + 1 + 1 = 2.

The other possible triple is 2, 3, 4 but it has greater sum of recognitions, equal to 1 + 1 + 1 = 3.

In the second sample there is no triple of warriors knowing each other.
"""

def find_min_recognition_sum(n, m, pairs):
    from collections import defaultdict
    
    # Create a dictionary to store the adjacency list of each warrior
    adjacency_list = defaultdict(list)
    
    # Populate the adjacency list
    for a, b in pairs:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    
    min_sum = float('inf')
    found = False
    
    # Iterate through each warrior to find potential triples
    for key in adjacency_list:
        for e in adjacency_list[key]:
            if e in adjacency_list:
                for e2 in adjacency_list[e]:
                    if e2 in adjacency_list[key] and e2 in adjacency_list[e] and key in adjacency_list[e2]:
                        # Calculate the sum of recognitions for the triple (key, e, e2)
                        recognition_sum = (len(adjacency_list[key]) + 
                                           len(adjacency_list[e]) + 
                                           len(adjacency_list[e2]) - 6)
                        min_sum = min(min_sum, recognition_sum)
                        found = True
    
    return min_sum if found else -1