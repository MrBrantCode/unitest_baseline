"""
QUESTION:
Railroad Trip

There are N cities in the JOI country, numbered 1, 2, ..., and N, respectively. In addition, there are N − 1 railroads, which are numbered 1, 2, ..., and N − 1, respectively. The railroad i (1 ≤ i ≤ N − 1) connects the city i and the city i + 1 in both directions.

There are two ways to get on the JOI railway, one is to use a paper ticket and the other is to use an IC card.

* The fare for boarding the railway i with a paper ticket is Ai yen.
* The fare for boarding the railway i with an IC card is Bi Yen. However, in order to board the railway i with an IC card, it is necessary to purchase an IC card that can be used with the railway i in advance. It costs Ci yen to purchase an IC card that can be used on the railway i. Once purchased, the IC card can be used any number of times.



Since the IC card makes it easier to process the amount, the fare for boarding with an IC card is cheaper than the fare for boarding with a paper ticket. That is, for i = 1, 2, ..., N − 1, Ai> Bi holds. Since the specifications of IC cards are all different for each railroad, the IC card that can be used on railroad i cannot be used on other railroads for any i.

You decide to travel all over the JOI country. We plan to start from the city P1 and visit the cities in the order of P2, P3, ..., PM. The trip consists of an M-1 day journey. On day j (1 ≤ j ≤ M − 1), travel by rail from city Pj to city Pj + 1. At this time, it may move by connecting several railroads. You may also visit the same city more than once. The railroads in JOI are so fast that you can travel from any city to any city in a day.

You currently do not have an IC card for any railroad. You want to purchase some railroad IC cards in advance and minimize the cost of this trip, that is, the sum of the IC card purchase cost and the railroad fare you boarded.

Task

Given the number of cities in the JOI country, the itinerary of the trip, and the fare and IC card price for each railroad in the JOI country. At this time, create a program to find the minimum amount of money required for the trip.

input

Read the following data from standard input.

* On the first line, integers N and M are written with blanks as delimiters. Each of these represents that there are N cities in the JOI country and the trip consists of an M-1 day journey.
* On the second line, M integers P1, P2, ..., PM are written with a space as a delimiter. These represent the rail movement from city Pj to city Pj + 1 on day j (1 ≤ j ≤ M − 1).
* On the i-th line (1 ≤ i ≤ N − 1) of the following N − 1 lines, three integers Ai, Bi, and Ci are written separated by blanks. These indicate that the fare when boarding the railway i with a paper ticket is Ai yen, the fare when boarding with an IC card is Bi yen, and the amount of the IC card that can be used on the railway i is Ci yen.


output

On the standard output, output an integer that represents the minimum value of the travel amount in yen on one line.

Limits

All input data satisfy the following conditions.

* 2 ≤ N ≤ 100 000.
* 2 ≤ M ≤ 100 000.
* 1 ≤ Bi <Ai ≤ 100 000 (1 ≤ i ≤ N − 1).
* 1 ≤ Ci ≤ 100 000 (1 ≤ i ≤ N − 1).
* 1 ≤ Pj ≤ N (1 ≤ j ≤ M).
* Pj ≠ Pj + 1 (1 ≤ j ≤ M − 1).



Input / output example

Input example 1


4 4
1 3 2 4
120 90 100
110 50 80
250 70 130


Output example 1


550


In this case, the method to minimize the cost of travel is as follows.

* Purchase IC cards for Railroad 2 and Railroad 3. This costs 80 + 130 = 210 yen.
* On the first day, move from city 1 to city 2 using a paper ticket, and then move from city 2 to city 3 using an IC card. This costs 120 + 50 = 170 yen.
* On the second day, move from city 3 to city 2 using an IC card. This costs 50 yen.
* On the third day, move from city 2 to city 3 using an IC card, and then move from city 3 to city 4 using an IC card. This costs 50 + 70 = 120 yen.



When moving in this way, the total amount of money spent on the trip is 210 + 170 + 50 + 120 = 550 yen. Since this is the minimum, it outputs 550.

Input example 2


8 5
7 5 3 5 4
12 5 8
16 2 1
3 1 5
17 12 17
19 7 5
12 2 19
4 1 3


Output example 2


81


The question text and the data used for the automatic referee are the question text and the test data for scoring, which are created and published by the Japan Committee for Information Olympics.





Example

Input

4 4
1 3 2 4
120 90 100
110 50 80
250 70 130


Output

550
"""

import itertools

def calculate_minimum_trip_cost(n, m, plst, abclst):
    sec = [0] * n
    for (pi, pi1) in zip(plst, plst[1:]):
        (p1, p2) = (min(pi, pi1) - 1, max(pi, pi1) - 1)
        sec[p1] += 1
        sec[p2] -= 1
    sec = tuple(itertools.accumulate(sec))
    ans = 0
    for i in range(n - 1):
        (a, b, c) = abclst[i]
        s = sec[i]
        ans += min(a * s, b * s + c)
    return ans