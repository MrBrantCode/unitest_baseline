"""
QUESTION:
Tokitsukaze and CSL are playing a little game of stones.

In the beginning, there are n piles of stones, the i-th pile of which has a_i stones. The two players take turns making moves. Tokitsukaze moves first. On each turn the player chooses a nonempty pile and removes exactly one stone from the pile. A player loses if all of the piles are empty before his turn, or if after removing the stone, two piles (possibly empty) contain the same number of stones. Supposing that both players play optimally, who will win the game?

Consider an example: n=3 and sizes of piles are a_1=2, a_2=3, a_3=0. It is impossible to choose the empty pile, so Tokitsukaze has two choices: the first and the second piles. If she chooses the first pile then the state will be [1, 3, 0] and it is a good move. But if she chooses the second pile then the state will be [2, 2, 0] and she immediately loses. So the only good move for her is to choose the first pile. 

Supposing that both players always take their best moves and never make mistakes, who will win the game?

Note that even if there are two piles with the same number of stones at the beginning, Tokitsukaze may still be able to make a valid first move. It is only necessary that there are no two piles with the same number of stones after she moves.

Input

The first line contains a single integer n (1 ≤ n ≤ 10^5) — the number of piles.

The second line contains n integers a_1, a_2, …, a_n (0 ≤ a_1, a_2, …, a_n ≤ 10^9), which mean the i-th pile has a_i stones.

Output

Print "sjfnb" (without quotes) if Tokitsukaze will win, or "cslnb" (without quotes) if CSL will win. Note the output characters are case-sensitive.

Examples

Input


1
0


Output


cslnb


Input


2
1 0


Output


cslnb


Input


2
2 2


Output


sjfnb


Input


3
2 3 1


Output


sjfnb

Note

In the first example, Tokitsukaze cannot take any stone, so CSL will win.

In the second example, Tokitsukaze can only take a stone from the first pile, and then, even though they have no stone, these two piles will have the same number of stones, which implies CSL will win.

In the third example, Tokitsukaze will win. Here is one of the optimal ways:

  * Firstly, Tokitsukaze can choose the first pile and take a stone from that pile. 
  * Then, CSL can only choose the first pile, because if he chooses the second pile, he will lose immediately. 
  * Finally, Tokitsukaze can choose the second pile, and then CSL will have no choice but to lose. 



In the fourth example, they only have one good choice at any time, so Tokitsukaze can make the game lasting as long as possible and finally win.
"""

def determine_winner(n, a):
    a = sorted(a)
    t = 0
    
    # Count pairs of piles with the same number of stones
    for i in range(1, n):
        t += a[i] == a[i - 1]
    
    # If there are more than 2 pairs, CSL wins
    if t >= 2:
        return 'cslnb'
    
    # If there is exactly one pair, check if it can be resolved
    if t:
        for i in range(n - 1):
            if a[i] == a[i + 1]:
                if a[i] and (i == 0 or a[i] != a[i - 1] + 1):
                    a[i] -= 1
                    break
                else:
                    return 'cslnb'
    
    # Calculate the sum of the differences and determine the winner based on parity
    total_sum = sum(a)
    expected_sum = n * (n - 1) // 2
    if (total_sum - expected_sum - t) % 2 == 1:
        return 'sjfnb'
    else:
        return 'cslnb'