"""
QUESTION:
D: Sunburn-Suntan-

story

Aizunyan is a second-year student who belongs to the programming contest club of Wakagamatsu High School, commonly known as the Prokon club. Cute like an angel. Aizu Nyan is planning to participate in this summer festival, so I made a schedule for the band to go to listen to. I'm worried about sunburn here. All live performances are held outdoors, but Aizu Nyan has a constitution that makes it easy to get sunburned, so if you are exposed to too much ultraviolet rays outdoors for a long time, you will get sunburned immediately. I plan to avoid UV rays as much as possible by evacuating indoors while there is no live performance, but during the live performance, it will inevitably hit the sun. Therefore, Aizu Nyan thought about taking measures against ultraviolet rays by applying sunscreen.

problem

If you apply sunscreen, you can get the effect for T minutes from the time you apply it. Sunscreen can only be applied once, so I want to use it effectively. Aizu Nyan is outdoors from the start time to the end time of the live, and is indoors at other times. You'll be given a live schedule that Aizu Nyan will listen to, so find the maximum amount of time you can get the sunscreen effect while you're outdoors.

Input format

The input can be given in the following format.


T
N
s_1 t_1
...
s_N t_N


The first line is given an integer T that represents the time it takes to get the sunscreen effect. The second line is given an integer N that represents the number of live concerts Aizu Nyan listens to. The following N lines are given the integer s_i, which represents the start time of the live that Aizu Nyan listens to thi, and the integer t_i, which represents the end time, separated by spaces.

Constraint

* 1 ≤ T ≤ 10 ^ {15}
* 1 ≤ N ≤ 10 ^ 5
* 0 ≤ s_i <t_i ≤ 10 ^ {15} (1 ≤ i ≤ N)
* The start time of the (i + 1) th live is the same as or later than the end time of the i-th live. That is, t_i ≤ s_ {i + 1} (1 ≤ i <N)



output

Print one line for the maximum amount of time you can get the sunscreen effect while you're outdoors.

Input example 1


20
1
0 10


Output example 1


Ten

Input example 2


20
1
0 100


Output example 2


20

Input example 3


9
3
1 5
9 11
13 20


Output example 3


7

Input example 4


twenty five
Five
9 12
15 20
21 25
28 40
45 60


Output example 4


twenty one





Example

Input

20
1
0 10


Output

10
"""

from bisect import bisect_left

def max_sunscreen_effect_time(T: int, N: int, schedules: list[tuple[int, int]]) -> int:
    a = [0]
    s = [0]
    t = [0]
    
    for _s, _t in schedules:
        s.append(_s)
        t.append(_t)
        a.append(a[-1] + _t - _s)
    
    s.append(1 << 62)
    t.append(1 << 62)
    
    ans = 0
    k = bisect_left(t, T, 0) - 1
    
    for i in range(1, N + 1):
        x = s[i] + T
        k = bisect_left(t, x, k) - 1
        y = a[k] - a[i - 1]
        
        if x > s[k + 1]:
            y += x - s[k + 1]
        
        if y > ans:
            ans = y
            if ans == T:
                break
    
    return ans