"""
QUESTION:
An expedition group flew from planet ACM-1 to Earth in order to study the bipedal species (its representatives don't even have antennas on their heads!).

The flying saucer, on which the brave pioneers set off, consists of three sections. These sections are connected by a chain: the 1-st section is adjacent only to the 2-nd one, the 2-nd one — to the 1-st and the 3-rd ones, the 3-rd one — only to the 2-nd one. The transitions are possible only between the adjacent sections.

The spacecraft team consists of n aliens. Each of them is given a rank — an integer from 1 to n. The ranks of all astronauts are distinct. The rules established on the Saucer, state that an alien may move from section a to section b only if it is senior in rank to all aliens who are in the segments a and b (besides, the segments a and b are of course required to be adjacent). Any alien requires exactly 1 minute to make a move. Besides, safety regulations require that no more than one alien moved at the same minute along the ship.

Alien A is senior in rank to alien B, if the number indicating rank A, is more than the corresponding number for B.

At the moment the whole saucer team is in the 3-rd segment. They all need to move to the 1-st segment. One member of the crew, the alien with the identification number CFR-140, decided to calculate the minimum time (in minutes) they will need to perform this task.

Help CFR-140, figure out the minimum time (in minutes) that all the astronauts will need to move from the 3-rd segment to the 1-st one. Since this number can be rather large, count it modulo m.

Input

The first line contains two space-separated integers: n and m (1 ≤ n, m ≤ 109) — the number of aliens on the saucer and the number, modulo which you should print the answer, correspondingly.

Output

Print a single number — the answer to the problem modulo m.

Examples

Input

1 10


Output

2


Input

3 8


Output

2

Note

In the first sample the only crew member moves from segment 3 to segment 2, and then from segment 2 to segment 1 without any problems. Thus, the whole moving will take two minutes.

To briefly describe the movements in the second sample we will use value <image>, which would correspond to an alien with rank i moving from the segment in which it is at the moment, to the segment number j. Using these values, we will describe the movements between the segments in the second sample: <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>, <image>; In total: the aliens need 26 moves. The remainder after dividing 26 by 8 equals 2, so the answer to this test is 2.
"""

def calculate_minimum_time(n: int, m: int) -> int:
    """
    Calculate the minimum time (in minutes) required for all aliens to move from the 3rd segment to the 1st segment, modulo m.

    Parameters:
    n (int): The number of aliens on the saucer.
    m (int): The modulo value to print the answer.

    Returns:
    int: The minimum time modulo m.
    """
    
    def binpow(a, n):
        res = 1
        while n > 0:
            if n & 1:
                res = res * a % m
            a = a * a % m
            n >>= 1
        return res
    
    ans = binpow(3, n) - 1
    if ans % m == 0 and ans != 0:
        return m - 1
    else:
        return ans % m