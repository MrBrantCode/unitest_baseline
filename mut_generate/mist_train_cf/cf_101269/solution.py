"""
QUESTION:
Create a function called `ernest_make_friends` that takes a list of tuples representing victims, where each tuple contains the victim's name and age. The function should return the minimum number of days it takes for Ernest to make friends with all eligible victims. A victim is eligible if their name starts with the letter "E" and their age is a prime number. Ernest can only approach one victim per day and cannot approach the same victim twice. If Ernest is unable to make friends with all eligible victims within 30 days, the function should return -1.
"""

import math

def ernest_make_friends(victims):
    approached = set()
    days = 0

    while len(approached) < len(victims) and days < 30:
        victim = next((v for v in victims if v[0][0] == "E" and v[1] > 1 and all(v[1] % i != 0 for i in range(2, int(math.sqrt(v[1]))+1)) and v not in approached), None)
        
        if victim is None:
            return -1
        
        approached.add(victim)
        days += 1

    return days