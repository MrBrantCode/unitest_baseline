"""
QUESTION:
You play a computer game. In this game, you lead a party of $m$ heroes, and you have to clear a dungeon with $n$ monsters. Each monster is characterized by its power $a_i$. Each hero is characterized by his power $p_i$ and endurance $s_i$.

The heroes clear the dungeon day by day. In the beginning of each day, you choose a hero (exactly one) who is going to enter the dungeon this day.

When the hero enters the dungeon, he is challenged by the first monster which was not defeated during the previous days (so, if the heroes have already defeated $k$ monsters, the hero fights with the monster $k + 1$). When the hero fights the monster, there are two possible outcomes:

  if the monster's power is strictly greater than the hero's power, the hero retreats from the dungeon. The current day ends;  otherwise, the monster is defeated. 

After defeating a monster, the hero either continues fighting with the next monster or leaves the dungeon. He leaves the dungeon either if he has already defeated the number of monsters equal to his endurance during this day (so, the $i$-th hero cannot defeat more than $s_i$ monsters during each day), or if all monsters are defeated — otherwise, he fights with the next monster. When the hero leaves the dungeon, the current day ends.

Your goal is to defeat the last monster. What is the minimum number of days that you need to achieve your goal? Each day you have to use exactly one hero; it is possible that some heroes don't fight the monsters at all. Each hero can be used arbitrary number of times.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10^5$) — the number of test cases. Then the test cases follow.

The first line of each test case contains one integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the number of monsters in the dungeon.

The second line contains $n$ integers $a_1$, $a_2$, ..., $a_n$ ($1 \le a_i \le 10^9$), where $a_i$ is the power of the $i$-th monster.

The third line contains one integer $m$ ($1 \le m \le 2 \cdot 10^5$) — the number of heroes in your party.

Then $m$ lines follow, each describing a hero. Each line contains two integers $p_i$ and $s_i$ ($1 \le p_i \le 10^9$, $1 \le s_i \le n$) — the power and the endurance of the $i$-th hero.

It is guaranteed that the sum of $n + m$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case print one integer — the minimum number of days you have to spend to defeat all of the monsters (or $-1$ if it is impossible).


-----Example-----
Input
2
6
2 3 11 14 1 8
2
3 2
100 1
5
3 5 100 2 3
2
30 5
90 1

Output
5
-1
"""

def minimum_days_to_clear_dungeon(n, monsters, m, heroes):
    # Initialize the day array to store the maximum power of heroes for each endurance level
    day = [0] * (n + 1)
    
    # Update the day array with the maximum power of heroes for each endurance level
    for p, s in heroes:
        day[s] = max(day[s], p)
    
    # Propagate the maximum power values backwards to ensure day[i] is the maximum power
    # for endurance i or more
    for i in range(n - 1, -1, -1):
        day[i] = max(day[i], day[i + 1])
    
    # If the maximum monster power is greater than the maximum power of any hero,
    # it is impossible to clear the dungeon
    if max(monsters) > day[0]:
        return -1
    
    # Construct the sparse table for range maximum query
    dp = cons(n, monsters)
    
    # Initialize variables for the binary search and counting days
    val = 0
    i = 0
    
    # Use binary search to find the minimum number of days required
    while i != n:
        hi, lo, ans = n - 1, i, i
        while hi >= lo:
            mid = (hi + lo) // 2
            maxi = ask(i, mid, dp)
            if day[mid - i + 1] >= maxi:
                lo = mid + 1
                ans = mid
            else:
                hi = mid - 1
        i = ans + 1
        val += 1
    
    return val

# Helper functions for constructing the sparse table and querying it
def cons(n, x):
    xx = n.bit_length()
    dp = [[0] * n for _ in range(xx)]
    dp[0] = x
    for i in range(1, xx):
        for j in range(n - (1 << i) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + (1 << i - 1)])
    return dp

def ask(l, r, dp):
    xx1 = (r - l + 1).bit_length() - 1
    return max(dp[xx1][l], dp[xx1][r - (1 << xx1) + 1])