"""
QUESTION:
As you know, all the kids in Berland love playing with cubes. Little Petya has n towers consisting of cubes of the same size. Tower with number i consists of a_{i} cubes stacked one on top of the other. Petya defines the instability of a set of towers as a value equal to the difference between the heights of the highest and the lowest of the towers. For example, if Petya built five cube towers with heights (8, 3, 2, 6, 3), the instability of this set is equal to 6 (the highest tower has height 8, the lowest one has height 2). 

The boy wants the instability of his set of towers to be as low as possible. All he can do is to perform the following operation several times: take the top cube from some tower and put it on top of some other tower of his set. Please note that Petya would never put the cube on the same tower from which it was removed because he thinks it's a waste of time. 

Before going to school, the boy will have time to perform no more than k such operations. Petya does not want to be late for class, so you have to help him accomplish this task.


-----Input-----

The first line contains two space-separated positive integers n and k (1 ≤ n ≤ 100, 1 ≤ k ≤ 1000) — the number of towers in the given set and the maximum number of operations Petya can perform. The second line contains n space-separated positive integers a_{i} (1 ≤ a_{i} ≤ 10^4) — the towers' initial heights.


-----Output-----

In the first line print two space-separated non-negative integers s and m (m ≤ k). The first number is the value of the minimum possible instability that can be obtained after performing at most k operations, the second number is the number of operations needed for that.

In the next m lines print the description of each operation as two positive integers i and j, each of them lies within limits from 1 to n. They represent that Petya took the top cube from the i-th tower and put in on the j-th one (i ≠ j). Note that in the process of performing operations the heights of some towers can become equal to zero.

If there are multiple correct sequences at which the minimum possible instability is achieved, you are allowed to print any of them.


-----Examples-----
Input
3 2
5 8 5

Output
0 2
2 1
2 3

Input
3 4
2 2 4

Output
1 1
3 2

Input
5 3
8 3 2 6 3

Output
3 3
1 3
1 2
1 3



-----Note-----

In the first sample you need to move the cubes two times, from the second tower to the third one and from the second one to the first one. Then the heights of the towers are all the same and equal to 6.
"""

def minimize_tower_instability(n, k, heights):
    # Create a list of towers with their initial heights and indices
    towers = [[heights[i], i + 1] for i in range(n)]
    towers.sort()
    
    operations = []
    k1 = k
    
    # If all towers are already of the same height, no operations are needed
    if len(set(heights)) == 1:
        return 0, 0, []
    
    # Perform operations to minimize instability
    while k > 0:
        k -= 1
        # Move a cube from the tallest tower to the shortest tower
        towers[0][0] += 1
        towers[-1][0] -= 1
        operations.append((towers[-1][1], towers[0][1]))
        towers.sort()
        
        # Check if all towers are of the same height
        if len(set((towers[i][0] for i in range(n)))) == 1:
            break
    
    # Calculate the final heights of the towers
    final_heights = [towers[i][0] for i in range(n)]
    
    # Calculate the minimum instability
    min_instability = max(final_heights) - min(final_heights)
    
    return min_instability, len(operations), operations