"""
QUESTION:
Takahashi recorded his daily life for the last few days as a integer sequence of length 2N, as follows:

* a_1, b_1, a_2, b_2, ... , a_N, b_N



This means that, starting from a certain time T, he was:

* sleeping for exactly a_1 seconds
* then awake for exactly b_1 seconds
* then sleeping for exactly a_2 seconds
* :
* then sleeping for exactly a_N seconds
* then awake for exactly b_N seconds



In this record, he waked up N times.

Takahashi is wondering how many times he waked up early during the recorded period.

Here, he is said to wake up early if he wakes up between 4:00 AM and 7:00 AM, inclusive.

If he wakes up more than once during this period, each of these awakenings is counted as waking up early.

Unfortunately, he forgot the time T.

Find the maximum possible number of times he waked up early during the recorded period.

For your information, a day consists of 86400 seconds, and the length of the period between 4:00 AM and 7:00 AM is 10800 seconds.

Constraints

* 1 \leq N \leq 10^5
* 1 \leq a_i, b_i \leq 10^5
* a_i and b_i are integers.

Input

The input is given from Standard Input in the following format:


N
a_1 b_1
a_2 b_2
:
a_N b_N


Output

Print the maximum possible number of times he waked up early during the recorded period.

Examples

Input

3
28800 57600
28800 57600
57600 28800


Output

2


Input

10
28800 57600
4800 9600
6000 1200
600 600
300 600
5400 600
6000 5760
6760 2880
6000 12000
9000 600


Output

5
"""

def calculate_max_early_wakes(N, sleep_wake_pairs):
    x = []
    num = 0
    
    for a, b in sleep_wake_pairs:
        x.append((num + a) % 86400)
        num = (num + a + b) % 86400
    
    x = sorted(x)
    ans = 0
    
    from bisect import bisect
    
    for i in range(N):
        ans = max(ans, bisect(x, x[i] + 10800) - i)
        if x[i] <= 10800:
            x.append(x[i] + 86400)
    
    return ans