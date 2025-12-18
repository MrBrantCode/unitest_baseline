"""
QUESTION:
The new camp by widely-known over the country Spring Programming Camp is going to start soon. Hence, all the team of friendly curators and teachers started composing the camp's schedule. After some continuous discussion, they came up with a schedule $s$, which can be represented as a binary string, in which the $i$-th symbol is '1' if students will write the contest in the $i$-th day and '0' if they will have a day off.

At the last moment Gleb said that the camp will be the most productive if it runs with the schedule $t$ (which can be described in the same format as schedule $s$). Since the number of days in the current may be different from number of days in schedule $t$, Gleb required that the camp's schedule must be altered so that the number of occurrences of $t$ in it as a substring is maximum possible. At the same time, the number of contest days and days off shouldn't change, only their order may change.

Could you rearrange the schedule in the best possible way?


-----Input-----

The first line contains string $s$ ($1 \leqslant |s| \leqslant 500\,000$), denoting the current project of the camp's schedule.

The second line contains string $t$ ($1 \leqslant |t| \leqslant 500\,000$), denoting the optimal schedule according to Gleb.

Strings $s$ and $t$ contain characters '0' and '1' only.


-----Output-----

In the only line print the schedule having the largest number of substrings equal to $t$. Printed schedule should consist of characters '0' and '1' only and the number of zeros should be equal to the number of zeros in $s$ and the number of ones should be equal to the number of ones in $s$.

In case there multiple optimal schedules, print any of them.


-----Examples-----
Input
101101
110

Output
110110
Input
10010110
100011

Output
01100011

Input
10
11100

Output
01


-----Note-----

In the first example there are two occurrences, one starting from first position and one starting from fourth position.

In the second example there is only one occurrence, which starts from third position. Note, that the answer is not unique. For example, if we move the first day (which is a day off) to the last position, the number of occurrences of $t$ wouldn't change.

In the third example it's impossible to make even a single occurrence.
"""

from collections import Counter

def maximize_substring_occurrences(s: str, t: str) -> str:
    def prefixsuffixmatch(s):
        pi_table = [0] * len(s)
        for i in range(1, len(s)):
            y = pi_table[i - 1]
            while s[i] != s[y] and y != 0:
                y = pi_table[y - 1]
            if s[i] == s[y]:
                y += 1
            pi_table[i] = y
        return pi_table

    def fillit(x):
        if '0' not in x:
            x['0'] = 0
        if '1' not in x:
            x['1'] = 0
        return x

    counter_s = fillit(Counter(s))
    counter_t = fillit(Counter(t))
    t_pi_table = prefixsuffixmatch(t)
    longest_match = t_pi_table[-1]
    repeating_part = t[longest_match:]
    counter_repeating_part = fillit(Counter(repeating_part))

    result = []

    if counter_s['0'] >= counter_t['0'] and counter_s['1'] >= counter_t['1']:
        result.append(t)
        counter_s['0'] -= counter_t['0']
        counter_s['1'] -= counter_t['1']

    if '0' in counter_repeating_part and '1' in counter_repeating_part:
        if counter_repeating_part['0'] > 0 and counter_repeating_part['1'] > 0:
            r = min(counter_s['0'] // counter_repeating_part['0'], counter_s['1'] // counter_repeating_part['1'])
            result.append(repeating_part * r)
            counter_s['0'] -= r * counter_repeating_part['0']
            counter_s['1'] -= r * counter_repeating_part['1']

    result.append('0' * counter_s['0'])
    result.append('1' * counter_s['1'])

    return ''.join(result)