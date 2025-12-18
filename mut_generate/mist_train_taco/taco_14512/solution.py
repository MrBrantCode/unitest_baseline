"""
QUESTION:
Akash is feeling lonely.So he decided to visit his friend's house.
His friend's house is located at the distance of K metres  from his
house.Now,he can take a step of one metre ,two metres or three 
metres  at a time.Can you tell me number of ways of reaching
Akash's friend house.
As the answer can be large Print  answer mod 1000000007

Input

First line contains an integer t  denoting number of test cases 
Next t lines contains an integer k 

Output

Print t lines containing number of ways to to reach  friend's house modulo 1000000007

SAMPLE INPUT
2
2
3

SAMPLE OUTPUT
2
4
"""

def count_ways_to_reach(k: int) -> int:
    MOD = 1000000007
    if k <= 0:
        return 0
    if k == 1:
        return 1
    if k == 2:
        return 2
    if k == 3:
        return 4
    
    dis = [0] * k
    dis[0] = 1
    dis[1] = 2
    dis[2] = 4
    
    for i in range(3, k):
        dis[i] = (dis[i-1] + dis[i-2] + dis[i-3]) % MOD
    
    return dis[k-1]