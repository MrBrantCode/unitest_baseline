"""
QUESTION:
Vladik often travels by trains. He remembered some of his trips especially well and I would like to tell you about one of these trips:

Vladik is at initial train station, and now n people (including Vladik) want to get on the train. They are already lined up in some order, and for each of them the city code a_{i} is known (the code of the city in which they are going to).

Train chief selects some number of disjoint segments of the original sequence of people (covering entire sequence by segments is not necessary). People who are in the same segment will be in the same train carriage. The segments are selected in such way that if at least one person travels to the city x, then all people who are going to city x should be in the same railway carriage. This means that they can’t belong to different segments. Note, that all people who travel to the city x, either go to it and in the same railway carriage, or do not go anywhere at all.

Comfort of a train trip with people on segment from position l to position r is equal to XOR of all distinct codes of cities for people on the segment from position l to position r. XOR operation also known as exclusive OR.

Total comfort of a train trip is equal to sum of comfort for each segment.

Help Vladik to know maximal possible total comfort.


-----Input-----

First line contains single integer n (1 ≤ n ≤ 5000) — number of people.

Second line contains n space-separated integers a_1, a_2, ..., a_{n} (0 ≤ a_{i} ≤ 5000), where a_{i} denotes code of the city to which i-th person is going.


-----Output-----

The output should contain a single integer — maximal possible total comfort.


-----Examples-----
Input
6
4 4 2 5 2 3

Output
14

Input
9
5 1 3 1 5 2 4 2 5

Output
9



-----Note-----

In the first test case best partition into segments is: [4, 4] [2, 5, 2] [3], answer is calculated as follows: 4 + (2 xor 5) + 3 = 4 + 7 + 3 = 14

In the second test case best partition into segments is: 5 1 [3] 1 5 [2, 4, 2] 5, answer calculated as follows: 3 + (2 xor 4) = 3 + 6 = 9.
"""

def calculate_maximal_comfort(n, a):
    inf = 1 << 30
    maxi = max(a)
    f = [-1] * (maxi + 1)
    
    for i in range(n):
        if f[a[i]] == -1:
            f[a[i]] = i
    
    l = [-1] * (maxi + 1)
    for i in range(n - 1, -1, -1):
        if l[a[i]] == -1:
            l[a[i]] = i
    
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i - 1 == l[a[i - 1]]:
            min_l = f[a[i - 1]]
            max_r = i - 1
            used = set()
            v = 0
            for j in range(i - 1, -1, -1):
                min_l = min(min_l, f[a[j]])
                max_r = max(max_r, l[a[j]])
                if a[j] not in used:
                    v ^= a[j]
                    used.add(a[j])
                if max_r > i - 1:
                    break
                if j == min_l:
                    dp[i] = max(dp[i], dp[j] + v)
                    break
    
    return dp[n]