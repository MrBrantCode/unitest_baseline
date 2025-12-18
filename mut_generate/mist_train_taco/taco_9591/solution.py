"""
QUESTION:
Training is indispensable for achieving good results at ICPC. Rabbit wants to win at ICPC, so he decided to practice today as well.

Today's training is to use the Amidakuji to improve luck by gaining the ability to read the future. Of course, not only relying on intuition, but also detailed probability calculation is indispensable.

The Amidakuji we consider this time consists of N vertical bars with a length of H + 1 cm. The rabbit looks at the top of the stick and chooses one of the N. At the bottom of the bar, "hit" is written only at the location of the Pth bar from the left. The Amidakuji contains several horizontal bars. Consider the following conditions regarding the arrangement of horizontal bars.

* Each horizontal bar is at a height of a centimeter from the top of the vertical bar, where a is an integer greater than or equal to 1 and less than or equal to H.
* Each horizontal bar connects only two adjacent vertical bars.
* There are no multiple horizontal bars at the same height.



The rabbit drew M horizontal bars to satisfy these conditions. Unfortunately, the rabbit has a good memory, so I remember all the hit positions and the positions of the horizontal bars, so I can't enjoy the Amidakuji. So I decided to have my friend's cat add more horizontal bars.

First, the rabbit chooses one of the N sticks, aiming for a hit. After that, the cat performs the following operations exactly K times.

* Randomly select one of the locations that meet the conditions specified above even if a horizontal bar is added. Here, it is assumed that every place is selected with equal probability. Add a horizontal bar at the selected location.



Then, it is determined whether the stick selected by the rabbit was a hit. The way to follow the bars is the same as the normal Amidakuji (every time you meet a horizontal bar, you move to the next vertical bar). Rabbits want to have a high probability of winning as much as possible.



Input


H N P M K
A1 B1
...
AM BM


In Ai, Bi (1 ≤ i ≤ M), the i-th horizontal bar drawn by the rabbit is at a height of Ai centimeters from the top of the vertical bar, and the second vertical bar from the left and Bi from the left. + An integer that represents connecting the first vertical bar.

2 ≤ H ≤ 500, 2 ≤ N ≤ 100, 1 ≤ P ≤ N, 1 ≤ M ≤ 100, 1 ≤ K ≤ 100, M + K ≤ H, 1 ≤ A1 <A2 <... <AM ≤ H, Satisfy 1 ≤ Bi ≤ N-1.

Output

Output the probability of winning in one line when the rabbit chooses a stick so that the probability of winning is maximized. Absolute errors of 10-6 or less are allowed.

Examples

Input

9 4 3 2 1
2 1
7 3


Output

0.571428571


Input

9 4 3 2 3
2 1
7 3


Output

0.375661376
"""

def calculate_winning_probability(H, N, P, M, K, initial_bars):
    A = [0] * H
    for a, b in initial_bars:
        A[a - 1] = b
    
    S = [[0] * N for _ in range(K + 1)]
    S[0][P - 1] = 1
    T = [[0] * N for _ in range(K + 1)]
    
    for i in range(H - 1, -1, -1):
        b = A[i]
        for j in range(K + 1):
            T[j][:] = S[j][:]
        if b > 0:
            for Si in S:
                (Si[b - 1], Si[b]) = (Si[b], Si[b - 1])
        else:
            for k in range(K):
                v = (K - k) / (H - M - k)
                for j in range(1, N - 1):
                    S[k + 1][j] += (T[k][j - 1] + T[k][j] * (N - 3) + T[k][j + 1]) / (N - 1) * v
                S[k + 1][0] += (T[k][0] * (N - 2) + T[k][1]) / (N - 1) * v
                S[k + 1][N - 1] += (T[k][N - 1] * (N - 2) + T[k][N - 2]) / (N - 1) * v
    
    return max(S[K])