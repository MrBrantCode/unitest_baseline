"""
QUESTION:
"Fukusekiken" is a popular ramen shop where you can line up. But recently, I've heard some customers say, "I can't afford to have vacant seats when I enter the store, even though I have a long waiting time." I'd like to find out why such dissatisfaction occurs, but I'm too busy to check the actual procession while the shop is open. However, since I know the interval and number of customers coming from many years of experience, I decided to analyze the waiting time based on that.

There are 17 seats in the store facing the counter. The store opens at noon, and customers come as follows.

* 100 groups from 0 to 99 will come.
* The i-th group will arrive at the store 5i minutes after noon.
* The number of people in the i-th group is 5 when i% 5 is 1, and 2 otherwise.
(x% y represents the remainder when x is divided by y.)
* The i-th group finishes the meal in 17 (i% 2) + 3 (i% 3) + 19 minutes when seated.



The arrival times, number of people, and meal times for the first 10 groups are as follows:

Group number | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
Arrival time (minutes later) | 0 | 5 | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 45
Number of people (people) | 2 | 5 | 2 | 2 | 2 | 2 | 5 | 2 | 2 | 2
Meal time (minutes) | 19 | 39 | 25 | 36 | 22 | 42 | 19 | 39 | 25 | 36



In addition, when guiding customers to their seats, we do the following.

* Seats are numbered from 0 to 16.
* A group of x people can only be seated when there are x open seats in a row.



Also, if there are multiple places to sit, sit in the place with the lowest seat number. For example, if only seats 0, 1, 2, 4, and 5 are available, a group of 5 people cannot be seated. If you are in a group of two, you will be seated at number 0 and 1.

* Once you are seated, you will not be asked to move your seat.
* Customers come and go in 1 minute increments. At each time, we will guide customers in the following order.
1. The next group can be seated at the same time as the previous group leaves.
2. When seating customers, seat as many groups as possible at the same time, starting with the group at the top of the line. It does not overtake the order of the matrix. In other words, if the first group cannot be seated, even if other groups in the procession can be seated, they will not be seated.
3. Groups arriving at that time will line up at the end of the procession, if any. If there is no line and you can sit down, you will be seated, and if you cannot, you will wait in line. As an example, the following shows how the first 10 groups arrive. From left to right, the three columns in each row show the time, seating, and queue. For seats, the "_" is vacant and the number indicates that the group with that number is sitting in that seat.




Time: Seat procession
0: 00 _______________:
5: 0011111 ___________:
10: 001111122 ________:
15: 00111112233______:
18: 00111112233______:
19: __111112233______:
20: 44111112233 ______:
25: 4411111223355____:
30: 4411111223355____: 66666 Group 6 arrives
34: 4411111223355____: 66666
35: 4411111__3355____: 6666677 Group 7 arrives
40: 4411111__3355____: 666667788 Group 8 arrives
41: 4411111__3355____: 666667788
42: __11111__3355____: 666667788
43: __11111__3355____: 666667788
44: 6666677883355____: Groups 6, 7 and 8 are seated
45: 666667788335599__: Group 9 arrives and sits down


For example, at time 40, the eighth group arrives, but cannot be seated and joins the procession. The fourth group eats until time 41. At time 42, seats in the 4th group are available, but the 6th group is not yet seated due to the lack of consecutive seats. The first group eats until time 43. At time 44, the first group will be vacant, so the sixth group will be seated, and at the same time the seventh and eighth groups will be seated. The ninth group arrives at time 45 and will be seated as they are available.

Based on this information, create a program that outputs the time (in minutes) that the nth group of customers waits by inputting an integer n that is 0 or more and 99 or less.



Input

Given multiple datasets. Each dataset consists of one integer n.

The number of datasets does not exceed 20.

Output

For each dataset, print the minute wait time (integer greater than or equal to 0) for the nth customer on a single line.

Example

Input

5
6
7
8


Output

0
14
9
4
"""

import heapq
from collections import deque

class Seat:
    def __init__(self, n):
        self.seat = '_' * n

    def get(self, num):
        i = self.seat.find('_' * num)
        if i != -1:
            self.seat = self.seat[0:i] + 'o' * num + self.seat[i + num:]
            return i
        return None

    def release(self, i, num):
        self.seat = self.seat[0:i] + '_' * num + self.seat[i + num:]

def calculate_waiting_time(n):
    if not (0 <= n <= 99):
        raise ValueError("Group number must be between 0 and 99 inclusive.")
    
    waiting_time = [-1] * 100
    NUM_OF_SEAT = 17
    seat = Seat(NUM_OF_SEAT)
    LEAVE = 0
    COME = 1
    in_out = []
    Q = deque()
    
    for group_id in range(100):
        if group_id % 5 == 1:
            num = 5
        else:
            num = 2
        heapq.heappush(in_out, (group_id * 5, COME, NUM_OF_SEAT + 1, group_id, num))
    
    while in_out:
        (time, event, start_seat, group_id, num) = heapq.heappop(in_out)
        if event == COME:
            Q.append((time, group_id, num))
        else:
            seat.release(start_seat, num)
        
        while Q:
            res = seat.get(Q[0][2])
            if res is not None:
                (arrive, group_id, num) = Q.popleft()
                waiting_time[group_id] = time - arrive
                eating_time = 17 * (group_id % 2) + 3 * (group_id % 3) + 19
                heapq.heappush(in_out, (time + eating_time, LEAVE, res, group_id, num))
            else:
                break
    
    return waiting_time[n]