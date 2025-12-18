"""
QUESTION:
Training is indispensable for achieving good results at ICPC. Rabbit wants to win at ICPC, so he decided to practice today as well.

Today's training is to develop physical strength and judgment by running on a straight road. The rabbit is now standing at the starting line and looking out over a long, long road.

There are some carrots along the way, and rabbits can accelerate by eating carrots. Rabbits run at U meters per second when not accelerating, but by eating carrots, the speed is V meters per second from the last carrot eaten to T seconds later. Rabbits can also carry up to K carrots without eating them. Even if you have a carrot, the running speed does not change.

Assuming that it does not take long to bring and eat carrots, I would like to find the shortest time required to reach the goal.



Input


N K T U V L
D1
...
DN


N is the number of carrots, L is the distance from the start to the goal (meters), and Di (1 ≤ i ≤ N) is the distance from the start where the i-th carrot is located (meters).

1 ≤ N ≤ 200, 1 ≤ K ≤ N, 1 ≤ T ≤ 10,000, 1 ≤ U <V ≤ 10,000, 2 ≤ L ≤ 10,000, 0 <D1 <D2 <... <DN <L. All input values ​​are integers.

Output

Output the shortest required time (seconds) on one line. Absolute errors of 10-6 or less are allowed.

Examples

Input

1 1 1 2 3 100
50


Output

49.500000000


Input

3 1 1 2 3 100
49
50
51


Output

48.666666667
"""

def calculate_shortest_time(N, K, T, U, V, L, carrot_positions):
    ans = 0
    l = 0
    t = 0
    k = 0
    
    for i in range(N + 1):
        if i == N:
            d = L
        else:
            d = carrot_positions[i]
        
        length = d - l
        l = d
        
        while t > 0 or k > 0:
            if t > 0:
                if t * V >= length:
                    tmp = (t * V - length) / V
                    ans += t - tmp
                    t = tmp
                    if K > k:
                        k += 1
                    else:
                        t = T
                    length = 0
                    break
                else:
                    length = length - t * V
                    ans += t
                    t = 0
                    if k > 0:
                        k -= 1
                        t = T
            elif k > 0:
                k -= 1
                t = T
        
        if length > 0:
            ans += length / U
            if K > k:
                k += 1
            else:
                t = T
    
    return ans