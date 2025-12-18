"""
QUESTION:
At the pancake shop you work for, pancake dough is lined up in a row on an elongated iron plate and baked. Pancakes can be completed by turning them over with a spatula several times. How many times you turn it over to complete it depends on the pancake.

Since the spatula is large, two adjacent pancakes will be turned over at the same time. At this time, the positions of these two sheets do not switch. However, not only can you flip both ends together with the pancake next to you, but you can also flip just one. After turning over all the pancakes more than the required number of times, remove them all at once from the iron plate and you're done.

I don't want to flip the pancakes too much, as turning them over more than necessary will make them harder. So you wanted to find a way to minimize the total number of times each pancake was flipped over by the time it was all finished.

When each pancake is given the number of pancakes on the iron plate and how many times it must be turned over before it is completed, the number of times each pancake is turned over before it is completed (manipulate the spatula). Create a program that calculates the minimum sum of (not the number of times).



Input

The input is given in the following format.


N
p1 p2 ... pN


The number of pancakes N (3 ≤ N ≤ 5000) is given on the first line. The second line gives the number of flips pi (0 ≤ pi ≤ 3) required to complete each pancake.

Output

Output the minimum value of the total number of times each pancake is turned inside out on one line until all are completed.

Examples

Input

3
1 2 1


Output

4


Input

3
0 3 0


Output

6
"""

def minimize_pancake_flips(N, pancakes):
    ans = 10 ** 9
    for i in range(4):
        cnt = [0] * N
        cnt[0] += i
        for j in range(N - 1):
            diff = pancakes[j] - cnt[j]
            if diff > 0:
                cnt[j] += diff
                cnt[j + 1] += diff
        diff = pancakes[N - 1] - cnt[N - 1]
        if diff > 0:
            cnt[N - 1] += diff
        if ans > sum(cnt):
            ans = sum(cnt)
    return ans