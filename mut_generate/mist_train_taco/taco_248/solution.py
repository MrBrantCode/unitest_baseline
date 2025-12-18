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

from itertools import combinations

def minimal_carols_to_sing(lyrics, num_people):
    data = []
    for i in range(len(lyrics[0])):
        data.append([])
        for j in range(len(lyrics)):
            if lyrics[j][i] == 'Y':
                data[i].append(j)
    
    for i in range(1, len(data) + 1):
        a = combinations(data, i)
        for s in a:
            tem = set()
            for t in s:
                tem = tem.union(set(t))
            if len(tem) >= num_people:
                return i
    
    return num_people