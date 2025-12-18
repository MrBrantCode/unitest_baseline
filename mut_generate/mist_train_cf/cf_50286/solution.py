"""
QUESTION:
Predict the party that will finally announce the victory in the Dota2 senate voting procedure. Given a string `senate` where 'R' and 'D' represent the Radiant and Dire parties respectively, determine the winning party assuming each senator plays the best strategy for their own party. The length of the input string `senate` is between 1 and 10,000. Write a function `predictPartyVictory(senate)` that returns the winning party as either "Radiant" or "Dire".
"""

from collections import deque
def predictPartyVictory(senate):
    n = len(senate)
    radiant = deque()
    dire = deque()

    for i, s in enumerate(senate):
        if s == 'R':
            radiant.append(i)
        else:
            dire.append(i)

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()
        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)

    return "Radiant" if radiant else "Dire"