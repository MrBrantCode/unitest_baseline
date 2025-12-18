"""
QUESTION:
You work as a system administrator in a dormitory, which has $n$ rooms one after another along a straight hallway. Rooms are numbered from $1$ to $n$.

You have to connect all $n$ rooms to the Internet.

You can connect each room to the Internet directly, the cost of such connection for the $i$-th room is $i$ coins. 

Some rooms also have a spot for a router. The cost of placing a router in the $i$-th room is also $i$ coins. You cannot place a router in a room which does not have a spot for it. When you place a router in the room $i$, you connect all rooms with the numbers from $max(1,~i - k)$ to $min(n,~i + k)$ inclusive to the Internet, where $k$ is the range of router. The value of $k$ is the same for all routers. 

Calculate the minimum total cost of connecting all $n$ rooms to the Internet. You can assume that the number of rooms which have a spot for a router is not greater than the number of routers you have.


-----Input-----

The first line of the input contains two integers $n$ and $k$ ($1 \le n, k \le 2 \cdot 10^5$) — the number of rooms and the range of each router.

The second line of the input contains one string $s$ of length $n$, consisting only of zeros and ones. If the $i$-th character of the string equals to '1' then there is a spot for a router in the $i$-th room. If the $i$-th character of the string equals to '0' then you cannot place a router in the $i$-th room.


-----Output-----

Print one integer — the minimum total cost of connecting all $n$ rooms to the Internet.


-----Examples-----
Input
5 2
00100

Output
3

Input
6 1
000000

Output
21

Input
4 1
0011

Output
4

Input
12 6
000010000100

Output
15



-----Note-----

In the first example it is enough to place the router in the room $3$, then all rooms will be connected to the Internet. The total cost of connection is $3$.

In the second example you can place routers nowhere, so you need to connect all rooms directly. Thus, the total cost of connection of all rooms is $1 + 2 + 3 + 4 + 5 + 6 = 21$.

In the third example you need to connect the room $1$ directly and place the router in the room $3$. Thus, the total cost of connection of all rooms is $1 + 3 = 4$.

In the fourth example you need to place routers in rooms $5$ and $10$. Then all rooms will be connected to the Internet. The total cost of connection is $5 + 10 = 15$.
"""

def calculate_min_cost(n, k, s):
    inf = 10 ** 18
    who = [-1] * n
    
    # Mark the rooms that can be covered by a router placed in room i
    for i in range(n):
        if s[i] == '1':
            for j in range(min(n - 1, i + k), i - 1, -1):
                if who[j] == -1:
                    who[j] = i
                else:
                    break
    
    # Extend the coverage to the left side of the router
    for i in range(n):
        if s[i] == '1':
            for j in range(i - 1, max(-1, i - k - 1), -1):
                if who[j] == -1:
                    who[j] = i
                else:
                    break
    
    # Dynamic programming array to store the minimum cost
    dp = [inf] * (n + 1)
    dp[n] = 0
    
    # Calculate the minimum cost using dynamic programming
    for i in range(n, 0, -1):
        dp[i - 1] = min(dp[i - 1], dp[i] + i)
        if who[i - 1] != -1:
            dp[max(0, who[i - 1] - k)] = min(dp[max(0, who[i - 1] - k)], dp[i] + who[i - 1] + 1)
    
    return dp[0]