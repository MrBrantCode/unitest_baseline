"""
QUESTION:
In Programmers Army Land, people have started preparation as sports day is scheduled next week.
You are given a task to form 1 team of $k$ consecutive players, from a list of sports player whose powers are given to you.
You want your team to win this championship, so you have to chose your $k$ team players optimally i.e. there must not be any other $k$ consecutive team players who have their total power greater than your team members total power.

-----Input:-----
- The first line of the input contains a single integer $T$. $T$ denoting the number of test cases. The description of $T$ test cases is as follows.
- The next line of the input contains 2 space separated integers $N$ and $K$. $N$ denotes the total number of players and $K$ denotes the number of players allowed in a team.
- The next line of the input contains $N$ space-separated integers $A1, A2, A3...An$ where $ith$ number denotes power of $ith$ player.
Note: power of players can also be negative

-----Output:-----
- For each test-case print the total power that your selected team have(each test case output must be printed on a new line).

-----Constraints:-----
- $1 \leq T \leq 10^3$
- $1 \leq N,K \leq 10^5$
- $-10^7 \leq A1, A2, A3...An \leq 10^7$

-----Sample Input:-----
1
5 3
1 2 3 4 5

-----Sample Output:-----
12
"""

def find_max_team_power(arr, k):
    # Initialize the sum of the first k elements
    sumi = 0
    for j in range(k):
        sumi += arr[j]
    
    # Initialize the maximum sum found so far
    maxi = sumi
    
    # Use a sliding window to find the maximum sum of k consecutive elements
    for i in range(k, len(arr)):
        sumi -= arr[i - k]
        sumi += arr[i]
        maxi = max(maxi, sumi)
    
    return maxi