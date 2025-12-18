"""
QUESTION:
Masha works in an advertising agency. In order to promote the new brand, she wants to conclude contracts with some bloggers. In total, Masha has connections of $n$ different bloggers. Blogger numbered $i$ has $a_i$ followers.

Since Masha has a limited budget, she can only sign a contract with $k$ different bloggers. Of course, Masha wants her ad to be seen by as many people as possible. Therefore, she must hire bloggers with the maximum total number of followers.

Help her, find the number of ways to select $k$ bloggers so that the total number of their followers is maximum possible. Two ways are considered different if there is at least one blogger in the first way, which is not in the second way. Masha believes that all bloggers have different followers (that is, there is no follower who would follow two different bloggers).

For example, if $n=4$, $k=3$, $a=[1, 3, 1, 2]$, then Masha has two ways to select $3$ bloggers with the maximum total number of followers:

conclude contracts with bloggers with numbers $1$, $2$ and $4$. In this case, the number of followers will be equal to $a_1 + a_2 + a_4 = 6$.

conclude contracts with bloggers with numbers $2$, $3$ and $4$. In this case, the number of followers will be equal to $a_2 + a_3 + a_4 = 6$.

Since the answer can be quite large, output it modulo $10^9+7$.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 1000$) — the number of test cases. Then $t$ test cases follow.

The first line of each test case contains two integers $n$ and $k$ ($1 \le k \le n \le 1000$) — the number of bloggers and how many of them you can sign a contract with.

The second line of each test case contains $n$ integers $a_1, a_2, \ldots a_n$ ($1 \le a_i \le n$) — the number of followers of each blogger.

It is guaranteed that the sum of $n$ over all test cases does not exceed $1000$.


-----Output-----

For each test case, on a separate line output one integer — the number of ways to select $k$ bloggers so that the total number of their followers is maximum possible.


-----Examples-----

Input
3
4 3
1 3 1 2
4 2
1 1 1 1
2 1
1 2
Output
2
6
1


-----Note-----

The test case is explained in the statements.

In the second test case, the following ways are valid:

conclude contracts with bloggers with numbers $1$ and $2$. In this case, the number of followers will be equal to $a_1 + a_2 = 2$;

conclude contracts with bloggers with numbers $1$ and $3$. In this case, the number of followers will be equal to $a_1 + a_3 = 2$;

conclude contracts with bloggers with numbers $1$ and $4$. In this case, the number of followers will be equal to $a_1 + a_4 = 2$;

conclude contracts with bloggers with numbers $2$ and $3$. In this case, the number of followers will be equal to $a_2 + a_3 = 2$;

conclude contracts with bloggers with numbers $2$ and $4$. In this case, the number of followers will be equal to $a_2 + a_4 = 2$;

conclude contracts with bloggers with numbers $3$ and $4$. In this case, the number of followers will be equal to $a_3 + a_4 = 2$.

In the third test case, the following ways are valid:

concludes a contract with a blogger with the number $2$. In this case, the number of followers will be equal to $a_2 = 2$.
"""

def count_ways_to_select_bloggers(n, k, a):
    MOD = 1000000007
    
    # Sort the followers in descending order
    a.sort(reverse=True)
    
    # Select the top k bloggers
    top_k_followers = a[:k]
    
    # Find the minimum number of followers in the top k bloggers
    min_followers_in_top_k = min(top_k_followers)
    
    # Count how many times this minimum follower count appears in the top k bloggers
    count_min_in_top_k = top_k_followers.count(min_followers_in_top_k)
    
    # Count how many times this minimum follower count appears in the entire list
    count_min_in_all = a.count(min_followers_in_top_k)
    
    # Calculate the number of ways to choose count_min_in_top_k from count_min_in_all
    ways = 1
    for i in range(count_min_in_top_k):
        ways = (ways * (count_min_in_all - i)) % MOD
    for i in range(count_min_in_top_k):
        ways = (ways // (count_min_in_top_k - i)) % MOD
    
    return ways