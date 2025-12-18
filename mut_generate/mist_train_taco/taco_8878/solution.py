"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 
The Physics teacher in Tanu's class is teaching concepts of a bouncing ball. The rubber ball that she is using has the property that if the ball is dropped from height H then, it bounces back to maximum height H/F. So after first bounce it rises up to maximum height H/F, after second bounce to maximum height H/F^{2}, after third bounce to maximum height H/F^{3}, and so on.
The class has N children, and the teacher wants to select two children such that when the taller child drops the ball from his height, ball reaches a maximum height equal to the height of the shorter child after some (possibly zero) number of bounces. Note that zero bounces mean heights of the two children will be same. Given the heights of the children in the class Height[i], can you tell how many ways are there for the teacher to select two children for the demonstration? Note that when heights are same, the pair is only counted once (See first example for further clarification).

------ Input ------ 

First line contains T, number of testcases. Then 2*T lines follow, 2 per testcase.
First line of each testcase consists of two space-separated intergers N and F. Second line of each testcase contains N space-separated integers representing the array Height.

------ Output ------ 

For each testcase, print a single line containing the answer to the problem.

------ Constraints ------ 

$For 40 points: 1 ≤ T ≤ 100, 1 ≤ N ≤ 10^{3}, 2 ≤ F ≤ 10^{9}, 1 ≤ Height[i] ≤ 10^{9}
$$For 60 points: 1 ≤ T ≤ 100, 1 ≤ N ≤ 10^{4}, 2 ≤ F ≤ 10^{9}, 1 ≤ Height[i] ≤ 10^{9}$

----- Sample Input 1 ------ 
2
3 2
2 2 2
3 2
2 1 4
----- Sample Output 1 ------ 
3
3
----- explanation 1 ------ 
In the first case, the three pairs are (child 1, child 2), (child 2, child 3) and (child 1, child 3).
For the second case also, the three pairs are (child 1, child 2), (child 2, child 3) and (child 1, child 3).
"""

def count_bouncing_ball_pairs(N, F, heights):
    count = 0
    height_counts = {}
    
    # Reduce each height to its base form by dividing by F until it's no longer divisible
    base_heights = []
    for height in heights:
        base_height = height
        while base_height % F == 0:
            base_height //= F
        base_heights.append(base_height)
        if base_height not in height_counts:
            height_counts[base_height] = 0
        height_counts[base_height] += 1
    
    # Calculate the number of valid pairs
    for base_height in height_counts:
        count_of_height = height_counts[base_height]
        count += count_of_height * (count_of_height - 1) // 2
    
    return count