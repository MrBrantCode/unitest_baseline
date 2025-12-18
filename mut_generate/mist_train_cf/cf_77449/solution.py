"""
QUESTION:
Given a list of logs where each log represents a friendship event with a unique timestamp and the ids of two people, and the total number of people N, write a function `earliestAcq` that returns the earliest time when everyone became friends and the total number of unique friendships formed at that time. The function should take two parameters: `logs` and `N`, where `logs` is a list of lists containing the timestamp and the ids of two people who became friends, and `N` is the total number of people. If there is no such time, return [-1, total friendships]. The restrictions are: 2 <= N <= 10^5, 1 <= logs.length <= 10^6, 0 <= logs[i][0] <= 10^9, 0 <= logs[i][1], logs[i][2] <= N - 1, logs[i][1] != logs[i][2], and all timestamps in logs are different.
"""

def earliestAcq(logs, N):
    root = [-1]*N
    size = [1]*N
    logs.sort()
    count = 1
    friendships = 0
    def find(x):
        if root[x] < 0:
            return x
        root[x] = find(root[x])
        return root[x]
    for timestamp, a, b in logs:
        A = find(a)
        B = find(b)
        if A != B:
            friendships += 1
            if size[A] < size[B]:
                A, B = B, A
            root[B] = A
            size[A] += size[B]
            if size[A] == N:
                return [timestamp, friendships]
    return [-1, friendships]