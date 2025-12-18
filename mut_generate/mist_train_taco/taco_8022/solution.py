"""
QUESTION:
Some terrorist attacks on Indian border. Now Indian Army have to send his soldiers to fight against terrorist. There are total N soldiers in the camp. Every soldier has a skill denoted by a single character lies between A-Z (all skills are in CAPITAL LETTERS). Now commander gave order to stand all the soldiers in a row, so that he can select a segment of maximum number of soldiers from the row to sent them for fighting against the terrorist.

INPUT

First line contains number of test cases T, for each test case a single line represents soldiers standing in a row with their skill.

OUTPUT

A single line representing maximum number of soldiers that commander selects for each test case.

Constraints:

1 ≤ T ≤100

1 ≤ N ≤ 10000

SAMPLE INPUT
2
ABDEFGABEF
GHJKLMNOPQ

SAMPLE OUTPUT
6
10

Explanation

For first test case, the soldier skills are “ABDEFGABEF” maximum soldiers with different skills are “ABDEFG” and “BDEFGA”, "DEFGAB" with length 6.
"""

def find_max_unique_soldiers(soldiers_row: str) -> int:
    list1 = []
    count = 0
    
    for j in range(len(soldiers_row)):
        if soldiers_row[j] in list1:
            f = list1.index(soldiers_row[j])
            del list1[0:f+1]
        list1.append(soldiers_row[j])
        if len(list1) > count:
            count = len(list1)
    
    return count