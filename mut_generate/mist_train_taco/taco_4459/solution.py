"""
QUESTION:
Aika's house runs a small coffee shop. The scones baked by Aika's mother were very delicious and the shop was very prosperous.

One of the jobs of Aika, a waitress, is to deliver the scones that are baked one after another to the customer's seat. The baked scones are placed on a tray and lined up on the counter. Let Ki be the number of scones on the i-th tray. Aika must carry exactly m scones to each customer. Aika can have as many trays as she wants at a time, and can distribute scones from multiple trays to one customer, or from one tray to multiple customers.

There are so many customers coming to the coffee shop that even if you carry all the scones on the counter, you cannot deliver them to all of them. However, after reaching as many customers as possible, there may be less than m scones left over. Such scones will be given to Aika as a reward for helping.

Suddenly, Aika thought about it. If you deliver scones to customers with only some trays instead of having all the trays at once, the number of surplus scones will be different. With proper tray selection, you may be able to leave more scones. Aika decided to choose one continuous range of trays on the counter so that her mother wouldn't notice that she was deliberately choosing trays. Also, since the remaining trays are carried by fathers and mothers, Aika has only one chance to get scones.

By the way, how many scones can Aika get? Write a program to calculate. The number of trays n is 1 or more and 30,000 or less, and m is 1 or more and 100,000 or less. Also, each element Ki of the sequence is 0 or more and 232-1.



input

A sequence of multiple datasets is given as input. The end of the input is indicated by two lines of zeros. Each dataset is as follows.

1st line n m (integer integer; half-width space delimited)
2nd line Scone information on Obon K1 K2 ... Kn (all integers; half-width space delimited)
Ki: Number of scones on the i-th tray


The number of datasets does not exceed 50.

output

Outputs the maximum number of scones you can get for each dataset on one line.

Example

Input

5 11
11 27 34 45 56
8 5
0 2 1 5 4 6 8 3
5 2
2 4 2 4 6
10 18
10 15 12 31 12 50 11 23 43 181
1 100
5
0 0


Output

8
4
0
17
5
"""

def calculate_max_scones(n, m, trays):
    s = [0] * (n + 1)
    f = [-1] * m
    sum_scones = 0
    nmax = 0
    ans = 0
    
    for i in range(n):
        sum_scones += trays[i]
        trays[i] %= m
        if trays[i] > nmax:
            nmax = trays[i]
        if trays[i] == m - 1:
            ans = trays[i]
        s[i + 1] = s[i] + trays[i]
        if s[i + 1] >= m:
            s[i + 1] -= m
        f[s[i + 1]] = i + 1
    
    if ans == 0:
        if nmax == 0:
            ans = 0
        elif sum_scones < m:
            ans = sum_scones
        else:
            done = False
            for ans in range(m - 1, nmax - 1, -1):
                for i in range(n + 1):
                    x = s[i] + ans
                    if x >= m:
                        x -= m
                    if f[x] >= i:
                        done = True
                        break
                if done:
                    break
    
    return ans