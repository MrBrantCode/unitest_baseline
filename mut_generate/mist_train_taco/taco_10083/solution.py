"""
QUESTION:
The life goes up and down, just like nice sequences. Sequence t_1, t_2, ..., t_{n} is called nice if the following two conditions are satisfied:   t_{i} < t_{i} + 1 for each odd i < n;  t_{i} > t_{i} + 1 for each even i < n. 

For example, sequences (2, 8), (1, 5, 1) and (2, 5, 1, 100, 99, 120) are nice, while (1, 1), (1, 2, 3) and (2, 5, 3, 2) are not.

Bear Limak has a sequence of positive integers t_1, t_2, ..., t_{n}. This sequence is not nice now and Limak wants to fix it by a single swap. He is going to choose two indices i < j and swap elements t_{i} and t_{j} in order to get a nice sequence. Count the number of ways to do so. Two ways are considered different if indices of elements chosen for a swap are different.


-----Input-----

The first line of the input contains one integer n (2 ≤ n ≤ 150 000) — the length of the sequence.

The second line contains n integers t_1, t_2, ..., t_{n} (1 ≤ t_{i} ≤ 150 000) — the initial sequence. It's guaranteed that the given sequence is not nice.


-----Output-----

Print the number of ways to swap two elements exactly once in order to get a nice sequence.


-----Examples-----
Input
5
2 8 4 7 7

Output
2

Input
4
200 150 100 50

Output
1

Input
10
3 2 1 4 1 4 1 4 1 4

Output
8

Input
9
1 2 3 4 5 6 7 8 9

Output
0



-----Note-----

In the first sample, there are two ways to get a nice sequence with one swap:   Swap t_2 = 8 with t_4 = 7.  Swap t_1 = 2 with t_5 = 7. 

In the second sample, there is only one way — Limak should swap t_1 = 200 with t_4 = 50.
"""

def count_nice_sequence_swaps(n, sequence):
    if not n & 1:
        sequence.append(0)
    sequence.append(150001)
    
    fails = []
    res = 0
    a, b = 0, 150001
    
    for i, c in enumerate(sequence, -1):
        if i & 1:
            if a >= b or b <= c:
                if len(fails) > 5:
                    return 0
                fails.append(i)
        else:
            if a <= b or b >= c:
                if len(fails) > 5:
                    return 0
                fails.append(i)
        a, b = b, c
    
    ff = fails + [0]
    for i in fails:
        a = sequence[i]
        for j in range(n):
            sequence[i], sequence[j], ff[-1] = sequence[j], a, j
            if all((sequence[b - 1] < sequence[b] > sequence[b + 1] if b & 1 else sequence[b - 1] > sequence[b] < sequence[b + 1] for b in ff)):
                res += 1 if j in fails else 2
            sequence[j] = sequence[i]
        sequence[i] = a
    
    return res // 2