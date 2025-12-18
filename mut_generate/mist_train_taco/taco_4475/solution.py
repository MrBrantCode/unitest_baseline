"""
QUESTION:
A burglar got into a matches warehouse and wants to steal as many matches as possible. In the warehouse there are m containers, in the i-th container there are ai matchboxes, and each matchbox contains bi matches. All the matchboxes are of the same size. The burglar's rucksack can hold n matchboxes exactly. Your task is to find out the maximum amount of matches that a burglar can carry away. He has no time to rearrange matches in the matchboxes, that's why he just chooses not more than n matchboxes so that the total amount of matches in them is maximal.

Input

The first line of the input contains integer n (1 ≤ n ≤ 2·108) and integer m (1 ≤ m ≤ 20). The i + 1-th line contains a pair of numbers ai and bi (1 ≤ ai ≤ 108, 1 ≤ bi ≤ 10). All the input numbers are integer.

Output

Output the only number — answer to the problem.

Examples

Input

7 3
5 10
2 5
3 6


Output

62


Input

3 3
1 3
2 2
3 1


Output

7
"""

def max_matches_stolen(n, m, containers):
    # Sort containers by the number of matches per matchbox in descending order
    containers.sort(key=lambda x: x[1], reverse=True)
    
    max_matches = 0
    i = 0
    
    # Iterate through the sorted containers and calculate the maximum matches
    while n > 0 and i < m:
        ai, bi = containers[i]
        add = min(n, ai)
        max_matches += add * bi
        n -= add
        i += 1
    
    return max_matches