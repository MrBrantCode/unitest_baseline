"""
QUESTION:
Chefland has all the cities on a straight line. There are $N$ cities in Chefland numbered $1$ to $N$. City $i$ is located at coordinate $x_i$ on the x-axis. Guru wants to travel from city $A$ to city $B$. He starts at time t=0. He has following choices to travel.
- He can walk $1$ metre in $P$ secs.
- There is a train that travels from city $C$ to city $D$ which travels $1$ metre in $Q$ secs which starts at time t=$Y$ secs. Guru can take the train only at city $C$ and leave the train only at city $D$.
Can you help Guru find the minimum time he will need to travel from city $A$ to $B$. Note that you cannot board the train after time t =$Y$.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- First line of each testcase contains eight space separated integers $N, A, B, C, D, P, Q, Y $. 
- Second line of each testcase contains $N$ space-separated integers with the $i$-th integer representing $x_i$.

-----Output:-----
For each testcase, output in a single line containing the minimum travel time.

-----Constraints-----
- $1 \leq T \leq 300$
- $2 \leq N \leq 300$
- $-1000 \leq x_i \leq 1000$
- $0 \leq Y \leq 100000$
- $1 \leq A,B,C,D \leq n $
- $A \neq B$
- $C \neq D$
- $1 \leq P, Q \leq 100$
- $x_i < x_j$  if $i < j$

-----Sample Input:-----
1
4 1 3 2 4 3 2 4
1 2 3 4

-----Sample Output:-----
6

-----EXPLANATION:-----
Guru can walk directly in 6 secs.
If Guru takes train, then he will need  atleast 11 secs.
"""

def calculate_minimum_travel_time(N, A, B, C, D, P, Q, Y, x):
    # Calculate the direct walking time from A to B
    direct_walk_time = abs(x[B - 1] - x[A - 1]) * P
    
    # Calculate the time to reach city C from A by walking
    walk_to_train_time = abs(x[C - 1] - x[A - 1]) * P
    
    # Initialize the minimum time with the direct walking time
    min_time = direct_walk_time
    
    # Check if Guru can reach city C in time to catch the train
    if walk_to_train_time <= Y:
        # Calculate the total time if Guru takes the train
        train_travel_time = Y + abs(x[D - 1] - x[C - 1]) * Q + abs(x[B - 1] - x[D - 1]) * P
        # Update the minimum time if the train travel time is less
        min_time = min(min_time, train_travel_time)
    
    return min_time