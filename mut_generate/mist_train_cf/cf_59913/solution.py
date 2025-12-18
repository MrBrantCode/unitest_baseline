"""
QUESTION:
Create a function named `numFriendRequests` that takes an array `ages` of length between 1 and 20000 (inclusive) representing the ages of individuals. The age of each individual is between 1 and 120 (inclusive). The function should return the total number of friend requests that will be sent given the conditions:
- `age[B]` is less than or equal to half of `age[A]` plus 7
- `age[B]` is greater than `age[A]`
- `age[B]` is greater than 100 and `age[A]` is less than 100
Individuals will not send friend requests to themselves.
"""

def numFriendRequests(ages):
    count = [0] * 121
    for age in ages:
        count[age] += 1

    requests = 0
    for ageA, countA in enumerate(count):
        for ageB, countB in enumerate(count):
            if ageB <= ageA * 0.5 + 7 or ageB > ageA or (ageB > 100 and ageA < 100):
                continue
            requests += countA * countB
            if ageA == ageB:
                requests -= countA

    return requests