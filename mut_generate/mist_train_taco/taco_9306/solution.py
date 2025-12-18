"""
QUESTION:
There are N apartments along a number line, numbered 1 through N. Apartment i is located at coordinate X_i. Also, the office of AtCoder Inc. is located at coordinate S. Every employee of AtCoder lives in one of the N apartments. There are P_i employees who are living in Apartment i.

All employees of AtCoder are now leaving the office all together. Since they are tired from work, they would like to get home by the company's bus. AtCoder owns only one bus, but it can accommodate all the employees. This bus will leave coordinate S with all the employees and move according to the following rule:

* Everyone on the bus casts a vote on which direction the bus should proceed, positive or negative. (The bus is autonomous and has no driver.) Each person has one vote, and abstaining from voting is not allowed. Then, the bus moves a distance of 1 in the direction with the greater number of votes. If a tie occurs, the bus moves in the negative direction. If there is an apartment at the coordinate of the bus after the move, all the employees who live there get off.

* Repeat the operation above as long as there is one or more employees on the bus.




For a specific example, see Sample Input 1.

The bus takes one seconds to travel a distance of 1. The time required to vote and get off the bus is ignorable.

Every employee will vote so that he himself/she herself can get off the bus at the earliest possible time. Strictly speaking, when a vote is taking place, each employee see which direction results in the earlier arrival at his/her apartment, assuming that all the employees follow the same strategy in the future. Based on this information, each employee makes the optimal choice, but if either direction results in the arrival at the same time, he/she casts a vote to the negative direction.

Find the time the bus will take from departure to arrival at the last employees' apartment. It can be proved that, given the positions of the apartments, the numbers of employees living in each apartment and the initial position of the bus, the future movement of the bus is uniquely determined, and the process will end in a finite time.

Constraints

* 1 \leq N \leq 10^5
* 1 \leq S \leq 10^9
* 1 \leq X_1 < X_2 < ... < X_N \leq 10^9
* X_i \neq S ( 1 \leq i \leq N )
* 1 \leq P_i \leq 10^9 ( 1 \leq i \leq N )
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N S
X_1 P_1
X_2 P_2
:
X_N P_N


Output

Print the number of seconds the bus will take from departure to arrival at the last employees' apartment.

Examples

Input

3 2
1 3
3 4
4 2


Output

4


Input

6 4
1 10
2 1000
3 100000
5 1000000
6 10000
7 100


Output

21


Input

15 409904902
94198000 15017
117995501 7656764
275583856 313263626
284496300 356635175
324233841 607
360631781 148
472103717 5224
497641071 34695
522945827 816241
554305668 32
623788284 22832
667409501 124410641
876731548 12078
904557302 291749534
918215789 5


Output

2397671583
"""

def calculate_bus_travel_time(N, S, apartments):
    x = [apartment[0] for apartment in apartments]
    p = [apartment[1] for apartment in apartments]
    
    if x[0] > S:
        return x[-1] - S
    if x[-1] < S:
        return S - x[0]
    
    r = 0
    i = 0
    j = N - 1
    d = p[:]
    
    while i < j:
        if x[i] > S:
            break
        if x[j] < S:
            break
        if d[i] >= d[j]:
            d[i] += d[j]
            j -= 1
        else:
            d[j] += d[i]
            i += 1
    
    t = S
    k = sorted(list(zip(d, range(N))), reverse=True)
    lx = rx = S
    
    for (_, i) in k:
        if lx <= x[i] <= rx:
            continue
        if lx > x[i]:
            lx = x[i]
        else:
            rx = x[i]
        r += abs(t - x[i])
        t = x[i]
    
    return r