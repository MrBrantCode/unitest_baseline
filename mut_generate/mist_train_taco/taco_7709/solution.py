"""
QUESTION:
A daily train consists of N cars. Let's consider one particular car. It has 54 places numbered consecutively from 1 to 54, some of which are already booked and some are still free. The places are numbered in the following fashion:

The car is separated into 9 compartments of 6 places each, as shown in the picture. So, the 1st compartment consists of places 1, 2, 3, 4, 53 and 54, the 2nd compartment consists of places 5, 6, 7, 8, 51 and 52, and so on.

A group of X friends wants to buy tickets for free places, all of which are in one compartment (it's much funnier to travel together). You are given the information about free and booked places in each of the N cars. Find the number of ways to sell the friends exactly X tickets in one compartment (note that the order in which the tickets are sold doesn't matter).

-----Input-----
The first line of the input contains two integers X and N (1 ≤ X ≤ 6, 1 ≤ N ≤ 10) separated by a single space. Each of the following N lines contains the information about one car which is a string of length 54 consisting of '0' and '1'. The i-th character (numbered from 1) is '0' if place i in the corresponding car is free, and is '1' if place i is already booked.

-----Output-----
Output just one integer -- the requested number of ways.

-----Example-----
Input:
1 3
100101110000001011000001111110010011110010010111000101
001010000000101111100000000000000111101010101111111010
011110011110000001010100101110001011111010001001111010

Output:
85

Input:
6 3
100101110000001011000001111110010011110010010111000101
001010000000101111100000000000000111101010101111111010
011110011110000001010100101110001011111010001001111010

Output:
1

Input:
3 2
000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000

Output:
360

Explanation:
In the first test case, any of the free places can be sold. In the second test case, the only free compartment in the train is compartment 3 in the first car (places 9, 10, 11, 12, 49 and 50 are all free). In the third test case, the train is still absolutely free; as there are 20 ways to sell 3 tickets in an empty compartment, the answer is 2 * 9 * 20 = 360.
"""

from math import comb

def count_ways_to_book_tickets(X, N, car_seats):
    # Dictionary mapping compartment numbers to their respective seat indices
    dic = {
        1: [0, 1, 2, 3, 53, 52],
        2: [4, 5, 6, 7, 50, 51],
        3: [8, 9, 10, 11, 48, 49],
        4: [12, 13, 14, 15, 47, 46],
        5: [16, 17, 18, 19, 44, 45],
        6: [20, 21, 22, 23, 42, 43],
        7: [24, 25, 26, 27, 40, 41],
        8: [28, 29, 30, 31, 38, 39],
        9: [32, 33, 34, 35, 36, 37]
    }
    
    def count_ways_in_car(car_seat):
        net = 0
        for com in dic.values():
            count = sum(1 for xx in com if car_seat[xx] == '0')
            if count >= X:
                net += comb(count, X)
        return net
    
    total_ways = 0
    for car_seat in car_seats:
        total_ways += count_ways_in_car(car_seat)
    
    return total_ways