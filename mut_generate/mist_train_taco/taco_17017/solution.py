"""
QUESTION:
Algorithmic predicament - Bug Fixing #9

Oh no! Timmy's algorithim has gone wrong! help Timmy fix his algorithim! 

Task
Your task is to fix timmy's algorithim so it returns the group name with the highest total age. 

You will receive two groups of `people` objects, with two properties `name` and `age`. The name property is a string and the age property is a number.  
Your goal is to make the total the age of all people having the same name through both groups and return the name of the one with the highest age. If two names have the same total age return the first alphabetical name.
"""

from collections import Counter
from itertools import chain

def find_group_with_highest_age(persons1, persons2):
    c = Counter()
    for p in chain(persons1, persons2):
        c[p['name']] += p['age']
    return min(iter(c.items()), key=lambda n_a: (-n_a[1], n_a[0]))[0] if c else None