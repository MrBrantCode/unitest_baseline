"""
QUESTION:
Write a function `predictPartyVictory` that predicts the winning party in the Dota2 senate voting. The function takes a string `senate` representing the party affiliations of the senators, with 'R' for Radiant and 'D' for Dire. The function should return "Radiant" if the Radiant party wins and "Dire" if the Dire party wins. The length of the input string `senate` will be in the range [1, 10,000].
"""

def predictPartyVictory(senate):
    from collections import deque
    queue = deque()
    people = [0, 0]
    bans = [0, 0]
    
    for person in senate:
        x = person == 'R'
        people[x] += 1
        queue.append(x)

    while all(people):
        x = queue.popleft()
        if bans[x]:
            bans[x] -= 1
            people[x] -= 1
        else:
            bans[x^1] += 1
            queue.append(x)
            
    return "Radiant" if people[1] else "Dire"