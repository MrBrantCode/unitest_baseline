"""
QUESTION:
There is unrest in the Galactic Senate. Several thousand solar systems have declared their intentions to leave the Republic. Master Heidi needs to select the Jedi Knights who will go on peacekeeping missions throughout the galaxy. It is well-known that the success of any peacekeeping mission depends on the colors of the lightsabers of the Jedi who will go on that mission. 

Heidi has n Jedi Knights standing in front of her, each one with a lightsaber of one of m possible colors. She knows that for the mission to be the most effective, she needs to select some contiguous interval of knights such that there are exactly k_1 knights with lightsabers of the first color, k_2 knights with lightsabers of the second color, ..., k_{m} knights with lightsabers of the m-th color.

However, since the last time, she has learned that it is not always possible to select such an interval. Therefore, she decided to ask some Jedi Knights to go on an indefinite unpaid vacation leave near certain pits on Tatooine, if you know what I mean. Help Heidi decide what is the minimum number of Jedi Knights that need to be let go before she is able to select the desired interval from the subsequence of remaining knights.


-----Input-----

The first line of the input contains n (1 ≤ n ≤ 2·10^5) and m (1 ≤ m ≤ n). The second line contains n integers in the range {1, 2, ..., m} representing colors of the lightsabers of the subsequent Jedi Knights. The third line contains m integers k_1, k_2, ..., k_{m} (with $1 \leq \sum_{i = 1}^{m} k_{i} \leq n$) – the desired counts of Jedi Knights with lightsabers of each color from 1 to m.


-----Output-----

Output one number: the minimum number of Jedi Knights that need to be removed from the sequence so that, in what remains, there is an interval with the prescribed counts of lightsaber colors. If this is not possible, output  - 1.


-----Example-----
Input
8 3
3 3 1 2 2 1 1 3
3 1 1

Output
1
"""

def minimum_jedi_removals(n, m, lightsabers, desired_counts):
    INF = 1 << 60
    Constraint = [0] + desired_counts
    satisfied_color = 0
    
    for i in range(1, m + 1):
        if Constraint[i] == 0:
            satisfied_color += 1
    
    GETCOLOR = [0] * (n + 1)
    ans = INF
    waste = 0
    pos = 0
    
    for i in range(n):
        while satisfied_color < m and pos < n:
            now_color = lightsabers[pos]
            GETCOLOR[now_color] += 1
            if GETCOLOR[now_color] == Constraint[now_color]:
                satisfied_color += 1
            elif GETCOLOR[now_color] > Constraint[now_color]:
                waste += 1
            pos += 1
        
        if satisfied_color == m:
            ans = min(ans, waste)
        
        removed_color = lightsabers[i]
        if GETCOLOR[removed_color] > Constraint[removed_color]:
            GETCOLOR[removed_color] -= 1
            waste -= 1
            continue
        elif GETCOLOR[removed_color] == Constraint[removed_color]:
            GETCOLOR[removed_color] -= 1
            satisfied_color -= 1
    
    return ans if ans < INF else -1