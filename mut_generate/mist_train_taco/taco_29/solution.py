"""
QUESTION:
When little Petya grew up and entered the university, he started to take part in АСМ contests. Later he realized that he doesn't like how the АСМ contests are organised: the team could only have three members (and he couldn't take all his friends to the competitions and distribute the tasks between the team members efficiently), so he decided to organize his own contests PFAST Inc. — Petr and Friends Are Solving Tasks Corporation. PFAST Inc. rules allow a team to have unlimited number of members.

To make this format of contests popular he organised his own tournament. To create the team he will prepare for the contest organised by the PFAST Inc. rules, he chose several volunteers (up to 16 people) and decided to compile a team from them. Petya understands perfectly that if a team has two people that don't get on well, then the team will perform poorly. Put together a team with as many players as possible given that all players should get on well with each other.

Input

The first line contains two integer numbers n (1 ≤ n ≤ 16) — the number of volunteers, and m (<image>) — the number of pairs that do not get on. Next n lines contain the volunteers' names (each name is a non-empty string consisting of no more than 10 uppercase and/or lowercase Latin letters). Next m lines contain two names — the names of the volunteers who do not get on. The names in pair are separated with a single space. Each pair of volunteers who do not get on occurs exactly once. The strings are case-sensitive. All n names are distinct.

Output

The first output line should contain the single number k — the number of people in the sought team. Next k lines should contain the names of the sought team's participants in the lexicographical order. If there are several variants to solve the problem, print any of them. Petya might not be a member of the sought team. 

Examples

Input

3 1
Petya
Vasya
Masha
Petya Vasya


Output

2
Masha
Petya


Input

3 0
Pasha
Lesha
Vanya


Output

3
Lesha
Pasha
Vanya
"""

from collections import defaultdict
from itertools import combinations

def find_max_compatible_team(n, m, volunteers, enemies):
    # Create a dictionary to map names to indices and vice versa
    name_to_index = {volunteer: i for i, volunteer in enumerate(volunteers)}
    index_to_name = {i: volunteer for i, volunteer in enumerate(volunteers)}
    
    # Create a dictionary to store enemies
    enemy = defaultdict(set)
    for first, second in enemies:
        enemy[name_to_index[first]].add(name_to_index[second])
        enemy[name_to_index[second]].add(name_to_index[first])
    
    # Function to check if a team is compatible
    def is_compatible(team):
        for i in range(len(team)):
            for j in range(i + 1, len(team)):
                if team[j] in enemy[team[i]]:
                    return False
        return True
    
    # Initialize variables to store the best team
    best_team = []
    max_size = 0
    
    # Try all combinations of volunteers
    for size in range(1, n + 1):
        for comb in combinations(range(n), size):
            if is_compatible(comb):
                if size > max_size:
                    best_team = comb
                    max_size = size
    
    # Convert the best team indices back to names and sort them
    best_team_names = sorted(index_to_name[i] for i in best_team)
    
    return max_size, best_team_names