"""
QUESTION:
When the day begins, it's time to sing carols. Unfortunately, not all the family members know the lyrics to the same carols. Everybody knows at least one, though.
You are given a array of lyrics. The j-th character of the i-th element of lyrics is Y if the i-th person knows the j-th carol, and N if he doesn't. Print the minimal number of carols that must be sung to allow everyone to sing at least once.

Input:-
1st line contains number of testcases and next 2 lines of each testcases contains N and N no. of lyrics. 

Ouput:-
Print the minimal number of carols that must be sung to allow everyone to sing at least once.

SAMPLE INPUT
3
2
YN NY
3
YN YY YN
6
YNN YNY YNY NYY NYY NYN

SAMPLE OUTPUT
2
1
2
"""

def minimal_carols_to_sing(test_cases):
    results = []
    
    for case in test_cases:
        n, lyrics = case
        carol_count = len(lyrics[0])
        min_carols = carol_count
        
        for carol_index in range(carol_count):
            covered_people = set()
            for person_index in range(n):
                if lyrics[person_index][carol_index] == 'Y':
                    covered_people.add(person_index)
            if len(covered_people) == n:
                min_carols = 1
                break
        
        if min_carols == carol_count:
            for carol_index in range(carol_count):
                covered_people = set()
                current_carols = set()
                for person_index in range(n):
                    if lyrics[person_index][carol_index] == 'Y':
                        covered_people.add(person_index)
                        current_carols.add(carol_index)
                if len(covered_people) == n:
                    min_carols = min(min_carols, len(current_carols))
        
        results.append(min_carols)
    
    return results