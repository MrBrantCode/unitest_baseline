"""
QUESTION:
One must train much to do well on wizardry contests. So, there are numerous wizardry schools and magic fees.

One of such magic schools consists of n tours. A winner of each tour gets a huge prize. The school is organised quite far away, so one will have to take all the prizes home in one go. And the bags that you've brought with you have space for no more than k huge prizes.

Besides the fact that you want to take all the prizes home, you also want to perform well. You will consider your performance good if you win at least l tours.

In fact, years of organizing contests proved to the organizers that transporting huge prizes is an issue for the participants. Alas, no one has ever invented a spell that would shrink the prizes... So, here's the solution: for some tours the winner gets a bag instead of a huge prize. Each bag is characterized by number ai — the number of huge prizes that will fit into it.

You already know the subject of all tours, so you can estimate the probability pi of winning the i-th tour. You cannot skip the tour under any circumstances.

Find the probability that you will perform well on the contest and will be able to take all won prizes home (that is, that you will be able to fit all the huge prizes that you won into the bags that you either won or brought from home).

Input

The first line contains three integers n, l, k (1 ≤ n ≤ 200, 0 ≤ l, k ≤ 200) — the number of tours, the minimum number of tours to win, and the number of prizes that you can fit in the bags brought from home, correspondingly.

The second line contains n space-separated integers, pi (0 ≤ pi ≤ 100) — the probability to win the i-th tour, in percents.

The third line contains n space-separated integers, ai (1 ≤ ai ≤ 200) — the capacity of the bag that will be awarded to you for winning the i-th tour, or else -1, if the prize for the i-th tour is a huge prize and not a bag.

Output

Print a single real number — the answer to the problem. The answer will be accepted if the absolute or relative error does not exceed 10 - 6.

Examples

Input

3 1 0
10 20 30
-1 -1 2


Output

0.300000000000


Input

1 1 1
100
123


Output

1.000000000000

Note

In the first sample we need either win no tour or win the third one. If we win nothing we wouldn't perform well. So, we must to win the third tour. Other conditions will be satisfied in this case. Probability of wining the third tour is 0.3.

In the second sample we win the only tour with probability 1.0, and go back home with bag for it.
"""

from collections import defaultdict

def calculate_probability(n, l, k, pi, ai):
    m = ai.count(-1)
    x = {(0, min(k, m)): 1}
    r = [1]
    
    for p, s in zip(pi, ai):
        p /= 100
        if s > 0:
            y = defaultdict(int)
            for (k_val, a), q in x.items():
                y[k_val, a] += q - q * p
                a = min(m, a + s)
                k_val = min(l, k_val + 1)
                y[k_val, a] += q * p
            x = y
        else:
            i = [0] + [q * p for q in r]
            j = [q - q * p for q in r] + [0]
            r = [a + b for a, b in zip(i, j)]
    
    y = [[0] * (m + 1) for _ in range(n - m + 1)]
    for (k_val, a), q in x.items():
        if k_val + a >= l:
            y[k_val][a] = q
    
    for k_val in range(n - m, -1, -1):
        for a in range(m, 0, -1):
            y[k_val][a - 1] += y[k_val][a]
    
    for k_val in range(n - m, 0, -1):
        for a in range(m, -1, -1):
            y[k_val - 1][a] += y[k_val][a]
    
    d = 0
    for k_val, p in enumerate(r):
        if l - k_val <= n - m:
            d += y[max(0, l - k_val)][k_val] * p
    
    return d