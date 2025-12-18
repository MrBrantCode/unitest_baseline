"""
QUESTION:
B: Dansunau www --Dance Now!-

story

Last lab life! Daigakuin! !! Dosanko Snow has won 9th place in the event "Master Idol World", which can be said to be the outpost of the biggest competition "Lab Life" where master idols compete. The sharp dance is ridiculed as "9th place dance", and the whole body's deciding pose is also ridiculed as "9th place stance", which causes deep emotional wounds. In the upcoming Lab Life Preliminary Qualifying, we can never take 9th place ... Dosanko Snow, who renewed his determination, refined his special skill "self-control" and headed for the battlefield. ..

problem

A tournament "Lab Life" will be held in which N groups of units compete. In this tournament, the three divisions of Smile Pure Cool will be played separately, and the overall ranking will be decided in descending order of the total points scored in each game. The ranking of the smile category is determined in descending order of the smile value of each unit. Similarly, in the pure / cool category, the ranking is determined in descending order of pure / cool value. The score setting according to the ranking is common to all divisions, and the unit ranked i in a division gets r_i points in that division.

Here, if there are a plurality of units having the same value as the unit with the rank i, they are regarded as the same rate i rank, and the points r_i are equally obtained. More specifically, when k units are in the same ratio i position, k units get equal points r_i, and no unit gets points from r_ {i + 1} to r_ {i + k-1}. Also, the next largest unit (s) gets the score r_ {i + k}. As a specific example, consider a case where there are five units with smile values ​​of 1, 3, 2, 3, and 2, and 10, 8, 6, 4, and 2 points are obtained in descending order of rank. At this time, the 2nd and 4th units will get 10 points, the 3rd and 5th units will get 6 points, and the 1st unit will get 2 points.

Unit Dosanko Snow, who participates in the Lab Life Preliminary Qualifying, thinks that "Lab Life is not a play", so he entered the tournament first and became the first unit. However, when we obtained information on the smile value, pure value, and cool value (hereinafter referred to as 3 values) of all N groups participating in the tournament, we found that their overall ranking was (equal rate) 9th. Dosanko Snow can raise any one of the three values ​​by the special skill "Self Control", but if you raise it too much, you will get tired and it will affect the main battle, so you want to make the rise value as small as possible. Dosanko Snow wants to get out of 9th place anyway, so when you raise any one of the 3 values ​​by self-control so that it will be 8th or higher at the same rate, find the minimum value that needs to be raised.

Input format

The input is given in the following format.


N
r_1 ... r_N
s_1 p_1 c_1
...
s_N p_N c_N


The first line is given the integer N, which represents the number of units, in one line. The second line that follows is given N integers separated by blanks. The i (1 \ leq i \ leq N) th integer represents the score r_i that can be obtained when the ranking is i in each division. Of the following Nth line, the jth line is given three integers s_j, p_j, c_j. These represent the smile value s_j, pure value p_j, and cool value c_j of the jth unit, respectively. Dosanko Snow is the first unit.

Constraint

* 9 \ leq N \ leq 100
* 100 \ geq r_1> ...> r_N \ geq 1
* 1 \ leq s_j, p_j, c_j \ leq 100 (1 \ leq j \ leq N)
* Before self-control, Dosanko Snow was 9th (sometimes 9th, but never more than 8th)



Output format

By increasing any of the three values ​​by x by self-control, output the minimum x that makes Dosanko Snow 8th or higher at the same rate on one line. However, if self-control does not raise the ranking no matter how much you raise it, output "Saiko".

Input example 1


9
9 8 7 6 5 4 3 2 1
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
8 8 8
9 9 9


Output example 1


2

For example, if you raise the smile value by 2 by self-control, the rankings in each division of Dosanko Snow will be 7th, 9th, and 9th, respectively, and you will get 3 + 1 + 1 = 5 points. On the other hand, the ranking of the second unit in each division is 9th, 8th, and 8th, respectively, and 1 + 2 + 2 = 5 points are obtained. Since the other units get 6 points or more, these two units will be ranked 8th at the same rate, satisfying the conditions.

Input example 2


9
9 8 7 6 5 4 3 2 1
1 1 1
2 6 9
6 9 2
9 2 6
3 5 8
5 8 3
8 3 5
4 7 4
7 4 7


Output example 2


Saiko

No matter how much you raise the value, Dosanko Snow can only get up to 11 points, but other units can always get 14 points or more, so Dosanko Snow is immovable in 9th place.





Example

Input

9
9 8 7 6 5 4 3 2 1
1 1 1
2 2 2
3 3 3
4 4 4
5 5 5
6 6 6
7 7 7
8 8 8
9 9 9


Output

2
"""

def calculate_minimum_raise(N, R, SPC):
    def get_points(values, rankings):
        points = {}
        sorted_values = sorted(values, reverse=True)
        for value, rank in zip(sorted_values, rankings):
            if value not in points:
                points[value] = rank
        return points

    def calculate_total_points(SPC, pointS, pointP, pointC):
        return [pointS[s] + pointP[p] + pointC[c] for s, p, c in SPC]

    you = SPC[0]
    ans = 10 ** 5

    for i, value in enumerate(you):
        for delta in range(1, 102 - value):
            SPC[0][i] = value + delta
            S = [spc[0] for spc in SPC]
            P = [spc[1] for spc in SPC]
            C = [spc[2] for spc in SPC]

            pointS = get_points(S, R)
            pointP = get_points(P, R)
            pointC = get_points(C, R)

            total_points = calculate_total_points(SPC, pointS, pointP, pointC)
            if sorted(total_points, reverse=True).index(total_points[0]) != 8:
                ans = min(ans, delta)
                break

        SPC[0][i] = value

    return ans if ans != 10 ** 5 else 'Saiko'