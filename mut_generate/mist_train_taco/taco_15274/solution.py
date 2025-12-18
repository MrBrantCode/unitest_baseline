"""
QUESTION:
Hope you still have not forgotten about pig Benny.

She is asking for help again. 

This time you have to answer some queries that Benny will give you. 

All actions happen in the Universe where each planet has its own id starting from 0. There are infinite amount of planets.

To travel between different planets there are some special spacecrafts. Each spacecraft is characterized by the number di. 

If the id of the planet you are currently staying on is idj and you decided you use spacecraft with di you will go to planet with id equal to idj + di.

Benny's parents live nearby the planet with id equal to 0, so you may assume that there exists some spacecraft for which di is not more than 10^4.

You have to answer Q queries. Each query consists of one single integer x. You have to answer whether it's possible to go from planet with id equal to 0 to planet with id equal to x.

Constraints

1 ≤ N ≤ 10^3

1 ≤ Q ≤ 10^5

1 ≤ Di ≤ 10^9

1 ≤ X ≤ 10^9

Input

The first line contains two integers denoting N and Q.

The second line contains N integers denoting di  for spacecrafts. Numbers might be separated with more than one space and not more than 10.

The following Q lines contain single integer denoting xi.

SAMPLE INPUT
3 3
5 6 7
5
10
8

SAMPLE OUTPUT
YES
YES
NO

Explanation

You can reach 5 and 10 (5 + 5) and can not reach 8.
"""

def can_reach_planet(N, Q, arrD, queries):
    if N == 1:
        return ["YES" if x % arrD[0] == 0 else "NO" for x in queries]
    
    gcd = arrD[0]
    for i in range(1, N):
        b = arrD[i]
        while b:
            gcd, b = b, gcd % b
    
    if gcd > 1:
        arrD = [d // gcd for d in arrD]
    
    MAX = 1000000001
    mindiv = min(arrD)  # mindiv <= 10000
    
    if mindiv == 1:
        return ["YES" if x % gcd == 0 else "NO" for x in queries]
    else:
        minmods = {}
        for x in arrD:
            minmods[x % mindiv] = x if x % mindiv not in minmods else min(x, minmods[x % mindiv])
        
        arrD = [minmods[i] for i in minmods if i != 0]
        minmods = {}  # get back memory
        
        minOK = {}
        minOK[0] = 0
        modified = [0]
        
        while modified:
            old = modified
            modified = []
            for j in old:
                for d in arrD:
                    num = minOK[j] * mindiv + j + d
                    if num < MAX:
                        rem = num % mindiv
                        if not rem in minOK or minOK[rem] > num // mindiv:
                            minOK[rem] = num // mindiv
                            modified.append(rem)
        
        results = []
        for x in queries:
            if x % gcd != 0:
                results.append("NO")
            else:
                x //= gcd
                results.append("YES" if x % mindiv in minOK and minOK[x % mindiv] <= x // mindiv else "NO")
        
        return results