"""
QUESTION:
Alice is a geeky girl. She has a lot of codes to execute but she always choose a lucky time to execute a code. 
Time is shown in 24 hour format as hh:mm:ss
Time is said to be lucky if all the 6 characters (except ':') are different.

Given the time when she completed the code find a lucky time to execute it so that Alice need to wait as little as possible.

Input :

First line contains T, the number of test cases. Each of next T lines contains time when she completes a code (in format described above).

Output:

For each test case, output a single line containing lucky time (in format described above)

Constraints :

0 ≤  hh < 24

0 ≤ mm < 60

0 ≤  ss  < 60

SAMPLE INPUT
3
00:00:00
12:59:59
23:59:59

SAMPLE OUTPUT
01:23:45
13:02:45
01:23:45
"""

def find_lucky_time(current_time: str) -> str:
    def time_split(time_list):
        d1 = {}
        hh = int(time_list[0])
        mm = int(time_list[1])
        ss = int(time_list[2])
        d1['h1'] = hh // 10
        d1['h2'] = hh % 10
        d1['m1'] = mm // 10
        d1['m2'] = mm % 10
        d1['s1'] = ss // 10
        d1['s2'] = ss % 10
        return d1

    def clocktick(dict1):
        ss = dict1['s1'] * 10 + dict1['s2']
        mm = dict1['m1'] * 10 + dict1['m2']
        hh = dict1['h1'] * 10 + dict1['h2']

        if ss < 59:
            ss += 1
        else:
            ss = 0
            if mm < 59:
                mm += 1
            else:
                mm = 0
                if hh < 23:
                    hh += 1
                else:
                    hh = 0

        dict1 = time_split([hh, mm, ss])
        return dict1

    d1 = {}
    time_set = set()

    l1 = current_time.split(':')
    d1 = time_split(l1)

    while True:
        time_set.update(list(d1.values()))
        if len(time_set) == 6:
            break
        else:
            d1 = clocktick(d1)
            time_set.clear()
            time_set.update(list(d1.values()))

    lucky_time = f"{d1['h1']}{d1['h2']}:{d1['m1']}{d1['m2']}:{d1['s1']}{d1['s2']}"
    return lucky_time