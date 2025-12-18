"""
QUESTION:
There are $n$ boxers, the weight of the $i$-th boxer is $a_i$. Each of them can change the weight by no more than $1$ before the competition (the weight cannot become equal to zero, that is, it must remain positive). Weight is always an integer number.

It is necessary to choose the largest boxing team in terms of the number of people, that all the boxers' weights in the team are different (i.e. unique).

Write a program that for given current values ​$a_i$ will find the maximum possible number of boxers in a team.

It is possible that after some change the weight of some boxer is $150001$ (but no more).


-----Input-----

The first line contains an integer $n$ ($1 \le n \le 150000$) — the number of boxers. The next line contains $n$ integers $a_1, a_2, \dots, a_n$, where $a_i$ ($1 \le a_i \le 150000$) is the weight of the $i$-th boxer.


-----Output-----

Print a single integer — the maximum possible number of people in a team.


-----Examples-----
Input
4
3 2 4 1

Output
4

Input
6
1 1 1 4 4 4

Output
5



-----Note-----

In the first example, boxers should not change their weights — you can just make a team out of all of them.

In the second example, one boxer with a weight of $1$ can be increased by one (get the weight of $2$), one boxer with a weight of $4$ can be reduced by one, and the other can be increased by one (resulting the boxers with a weight of $3$ and $5$, respectively). Thus, you can get a team consisting of boxers with weights of $5, 4, 3, 2, 1$.
"""

def max_unique_boxers(n, weights):
    from collections import defaultdict
    
    # Frequency dictionary to count occurrences of each weight
    freq = defaultdict(int)
    for weight in weights:
        freq[weight] += 1
    
    # Array to track the unique weights we can form
    unique_weights = [0] * 150002
    
    # Try to form unique weights by adjusting each weight by -1, 0, or +1
    for i in range(1, 150002):
        if i - 1 in freq and freq[i - 1] > 0:
            unique_weights[i] = 1
            freq[i - 1] -= 1
            continue
        if i in freq and freq[i] > 0:
            unique_weights[i] = 1
            freq[i] -= 1
            continue
        if i + 1 in freq and freq[i + 1] > 0:
            unique_weights[i] = 1
            freq[i + 1] -= 1
            continue
    
    # The result is the sum of all unique weights formed
    return sum(unique_weights)