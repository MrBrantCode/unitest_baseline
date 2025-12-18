"""
QUESTION:
Bob is an active user of the social network Faithbug. On this network, people are able to engage in a mutual friendship. That is, if $a$ is a friend of $b$, then $b$ is also a friend of $a$. Each user thus has a non-negative amount of friends.

This morning, somebody anonymously sent Bob the following link: graph realization problem and Bob wants to know who that was. In order to do that, he first needs to know how the social network looks like. He investigated the profile of every other person on the network and noted down the number of his friends. However, he neglected to note down the number of his friends. Help him find out how many friends he has. Since there may be many possible answers, print all of them.


-----Input-----

The first line contains one integer $n$ ($1 \leq n \leq 5 \cdot 10^5$), the number of people on the network excluding Bob. 

The second line contains $n$ numbers $a_1,a_2, \dots, a_n$ ($0 \leq a_i \leq n$), with $a_i$ being the number of people that person $i$ is a friend of.


-----Output-----

Print all possible values of $a_{n+1}$ — the amount of people that Bob can be friend of, in increasing order.

If no solution exists, output $-1$.


-----Examples-----
Input
3
3 3 3

Output
3 

Input
4
1 1 1 1

Output
0 2 4 

Input
2
0 2

Output
-1

Input
35
21 26 18 4 28 2 15 13 16 25 6 32 11 5 31 17 9 3 24 33 14 27 29 1 20 4 12 7 10 30 34 8 19 23 22

Output
13 15 17 19 21 



-----Note-----

In the first test case, the only solution is that everyone is friends with everyone. That is why Bob should have $3$ friends.

In the second test case, there are three possible solutions (apart from symmetries):   $a$ is friend of $b$, $c$ is friend of $d$, and Bob has no friends, or  $a$ is a friend of $b$ and both $c$ and $d$ are friends with Bob, or  Bob is friends of everyone. 

The third case is impossible to solve, as the second person needs to be a friend with everybody, but the first one is a complete stranger.
"""

def find_possible_friends_of_bob(n, friends_counts):
    friends_counts.sort(reverse=True)
    mod = sum(friends_counts) % 2
    counts = [0] * (n + 1)
    for count in friends_counts:
        counts[count] += 1
    cumcounts = [0] * (n + 1)
    cumcounts[0] = counts[0]
    for i in range(n):
        cumcounts[i + 1] = cumcounts[i] + counts[i + 1]
    partialsums = [0] * (n + 1)
    curr = 0
    for i in range(n):
        curr += (i + 1) * counts[i + 1]
        partialsums[i + 1] = curr
    partialsums.append(0)
    cumcounts.append(0)
    sumi = 0
    diffs = [0] * n
    altdiffs = [0] * n
    for i in range(n):
        sumi += friends_counts[i]
        rhs = i * (i + 1)
        if friends_counts[i] > i:
            rhs += partialsums[i] + (i + 1) * (n - i - 1 - cumcounts[i])
        else:
            rhs += partialsums[friends_counts[i] - 1] + friends_counts[i] * (n - i - 1 - cumcounts[friends_counts[i] - 1])
        diffs[i] = sumi - rhs
        rhs2 = (i + 1) * (i + 2)
        if friends_counts[i] > i + 1:
            rhs2 += partialsums[i + 1] + (i + 2) * (n - i - 1 - cumcounts[i + 1])
        else:
            rhs2 += partialsums[friends_counts[i] - 1] + friends_counts[i] * (n - i - 1 - cumcounts[friends_counts[i] - 1])
        altdiffs[i] = sumi - rhs2
    mini = max(diffs)
    maxi = -max(altdiffs)
    mini = max(mini, 0)
    maxi = min(maxi, n)
    possible_friends = []
    if mini % 2 != mod:
        mini += 1
    if maxi % 2 == mod:
        maxi += 1
    for guy in range(mini, maxi, 2):
        possible_friends.append(guy)
    if not possible_friends:
        return [-1]
    return possible_friends