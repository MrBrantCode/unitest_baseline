"""
QUESTION:
Shinya watched a program on TV called "Maya's Great Prophecy! Will the World End in 2012?" After all, I wasn't sure if the world would end, but I was interested in Maya's "long-term calendar," which was introduced in the program. The program explained as follows.

The Maya long-term calendar is a very long calendar consisting of 13 Baktuns (1872,000 days) in total, consisting of the units shown in the table on the right. One calculation method believes that the calendar begins on August 11, 3114 BC and ends on December 21, 2012, which is why the world ends on December 21, 2012. .. However, there is also the idea that 13 Baktun will be one cycle, and when the current calendar is over, a new cycle will be started.

| 1 kin = 1 day
1 winal = 20 kin
1 tun = 18 winals
1 Katun = 20 tons
1 Baktun = 20 Katun |
--- | --- | ---



"How many days will my 20th birthday be in the Maya calendar?" Shinya wanted to express various days in the Maya long-term calendar.

Now, instead of Shinya, create a program that converts between the Christian era and the Maya long-term calendar.



input

The input consists of multiple datasets. The end of the input is indicated by # 1 line. Each dataset is given in the following format:


b.ka.t.w.ki


Or


y.m.d


The dataset consists of one line containing one character string. b.ka.t.w.ki is the Mayan long-term date and y.m.d is the Christian era date. The units given are as follows.

Maya long calendar
b | Baktun | (0 ≤ b <13)
--- | --- | ---
ka | Katun | (0 ≤ ka <20)
t | Tun | (0 ≤ t <20)
w | Winal | (0 ≤ w <18)
ki | kin | (0 ≤ ki <20)

Year
y | year | (2012 ≤ y ≤ 10,000,000)
--- | --- | ---
m | month | (1 ≤ m ≤ 12)
d | day | (1 ≤ d ≤ 31)



The maximum value for a day in the Christian era depends on whether it is a large month, a small month, or a leap year (a leap year is a multiple of 4 that is not divisible by 100 or divisible by 400). The range of dates in the Maya long calendar is from 0.0.0.0.0 to 12.19.19.17.19. However, 0.0.0.0.0.0 of the Maya long-term calendar corresponds to 2012.12.21 of the Christian era. The range of dates in the Christian era is from 2012.12.21 to 10000000.12.31.

The number of datasets does not exceed 500.

output

When the input is the Western calendar, the Maya long calendar is output, and when the input is the Maya long calendar, the Western calendar is output in the same format as the input. As a result of converting the input year, even if the next cycle of the Maya long calendar is entered, it may be output in the format of b.ka.t.w.ki.

Example

Input

2012.12.31
2.12.16.14.14
7138.5.13
10.5.2.1.5
10000000.12.31
#


Output

0.0.0.0.10
3054.8.15
0.0.0.0.10
6056.2.29
8.19.3.13.2
"""

import datetime

def convert_date(date_str: str) -> str:
    time_std = datetime.date(2012, 12, 21)
    n_len = list(map(int, date_str.split('.')))
    
    if len(n_len) == 3:
        # Convert Christian era date to Maya long-term date
        year_keep = 0
        while n_len[0] > 9999:
            year_keep += 1
            n_len[0] -= 400
        ans = [0] * 5
        cal_date = datetime.date(n_len[0], n_len[1], n_len[2])
        date_dif = (cal_date - time_std).days + year_keep * 146097
        ans[0] = str(date_dif // (20 * 20 * 18 * 20) % 13)
        ans[1] = str(date_dif // (20 * 18 * 20) % 20)
        ans[2] = str(date_dif // (18 * 20) % 20)
        ans[3] = str(date_dif // 20 % 18)
        ans[4] = str(date_dif % 20)
        return '.'.join(ans)
    
    elif len(n_len) == 5:
        # Convert Maya long-term date to Christian era date
        past_date = (((n_len[0] * 20 + n_len[1]) * 20 + n_len[2]) * 18 + n_len[3]) * 20 + n_len[4]
        year_keep = past_date // 146097
        past_date = past_date % 146097
        ans = list(map(str, str(datetime.date(2012, 12, 21) + datetime.timedelta(days=past_date)).split('-')))
        ans[0] = str(int(ans[0]) + year_keep * 400)
        ans[1] = str(int(ans[1]))
        ans[2] = str(int(ans[2]))
        return '.'.join(ans)
    
    else:
        raise ValueError("Invalid date format")