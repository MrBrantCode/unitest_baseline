"""
QUESTION:
Three friends are going to meet each other. Initially, the first friend stays at the position $x = a$, the second friend stays at the position $x = b$ and the third friend stays at the position $x = c$ on the coordinate axis $Ox$.

In one minute each friend independently from other friends can change the position $x$ by $1$ to the left or by $1$ to the right (i.e. set $x := x - 1$ or $x := x + 1$) or even don't change it.

Let's introduce the total pairwise distance — the sum of distances between each pair of friends. Let $a'$, $b'$ and $c'$ be the final positions of the first, the second and the third friend, correspondingly. Then the total pairwise distance is $|a' - b'| + |a' - c'| + |b' - c'|$, where $|x|$ is the absolute value of $x$.

Friends are interested in the minimum total pairwise distance they can reach if they will move optimally. Each friend will move no more than once. So, more formally, they want to know the minimum total pairwise distance they can reach after one minute.

You have to answer $q$ independent test cases.


-----Input-----

The first line of the input contains one integer $q$ ($1 \le q \le 1000$) — the number of test cases.

The next $q$ lines describe test cases. The $i$-th test case is given as three integers $a, b$ and $c$ ($1 \le a, b, c \le 10^9$) — initial positions of the first, second and third friend correspondingly. The positions of friends can be equal.


-----Output-----

For each test case print the answer on it — the minimum total pairwise distance (the minimum sum of distances between each pair of friends) if friends change their positions optimally. Each friend will move no more than once. So, more formally, you have to find the minimum total pairwise distance they can reach after one minute.


-----Example-----
Input
8
3 3 4
10 20 30
5 5 5
2 4 3
1 1000000000 1000000000
1 1000000000 999999999
3 2 5
3 2 6

Output
0
36
0
0
1999999994
1999999994
2
4
"""

def minimum_total_pairwise_distance(a, b, c):
    positions = [a, b, c]
    positions.sort()
    
    # Calculate initial distances
    d1 = abs(positions[0] - positions[1])
    d2 = abs(positions[1] - positions[2])
    d3 = abs(positions[0] - positions[2])
    
    # If all positions are the same
    if d1 == 0 and d2 == 0 and d3 == 0:
        return 0
    
    # If all positions are different
    if d1 > 0 and d2 > 0 and d3 > 0:
        # Move optimally to minimize the total pairwise distance
        if d1 > d2:
            positions[0] += 1
            positions[1] -= 1
            positions[2] -= 1
        elif d1 < d2:
            positions[1] += 1
            positions[2] -= 1
            positions[0] += 1
        else:
            positions[0] += 1
            positions[2] -= 1
        
        # Recalculate distances after movement
        d1 = abs(positions[0] - positions[1])
        d2 = abs(positions[1] - positions[2])
        d3 = abs(positions[0] - positions[2])
        return d1 + d2 + d3
    
    # If two positions are the same
    if d1 == 0:
        # Move the third position to minimize the distance
        if positions[2] == positions[1] + 1:
            return 0
        else:
            return 2 * (positions[2] - positions[1] - 1)
    
    if d2 == 0:
        # Move the first position to minimize the distance
        if positions[0] == positions[1] - 1:
            return 0
        else:
            return 2 * (positions[1] - positions[0] - 1)
    
    if d3 == 0:
        # Move the middle position to minimize the distance
        if positions[1] == positions[0] + 1:
            return 0
        else:
            return 2 * (positions[1] - positions[0] - 1)

    return d1 + d2 + d3