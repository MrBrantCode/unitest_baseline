"""
QUESTION:
Given a 2D integer array logs where each logs[i] = [IDi, timei, actioni] and an integer k, calculate a 1-indexed array answer of size k such that answer[j] is the number of users whose user active minutes (UAM) equals j. UAM for a given user is defined as the number of unique minutes in which the user performed a unique action. 

Implement a function `findingUsersActiveMinutes` that takes logs and k as input and returns the answer array. The function must work with the following constraints:
- 1 <= logs.length <= 10^4
- 0 <= IDi <= 10^9
- 1 <= timei <= 10^5
- 1 <= actioni <= 10^5
- k is in the range [The maximum UAM for a user, 10^5]
"""

def findingUsersActiveMinutes(logs, k):
    uam = {}
    for log in logs:
        id = log[0]
        time = log[1]*10000+log[2]
        
        if id not in uam:
            uam[id] = set()
            
        uam[id].add(time)
        
    result = [0] * k
    for key in uam:
        count = len(uam[key])
        if count <= k: 
            result[count-1] += 1
    return result