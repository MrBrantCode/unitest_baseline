"""
QUESTION:
Consider 2n rows of the seats in a bus. n rows of the seats on the left and n rows of the seats on the right. Each row can be filled by two people. So the total capacity of the bus is 4n.

Consider that m (m ≤ 4n) people occupy the seats in the bus. The passengers entering the bus are numbered from 1 to m (in the order of their entering the bus). The pattern of the seat occupation is as below:

1-st row left window seat, 1-st row right window seat, 2-nd row left window seat, 2-nd row right window seat, ... , n-th row left window seat, n-th row right window seat.

After occupying all the window seats (for m > 2n) the non-window seats are occupied:

1-st row left non-window seat, 1-st row right non-window seat, ... , n-th row left non-window seat, n-th row right non-window seat.

All the passengers go to a single final destination. In the final destination, the passengers get off in the given order.

1-st row left non-window seat, 1-st row left window seat, 1-st row right non-window seat, 1-st row right window seat, ... , n-th row left non-window seat, n-th row left window seat, n-th row right non-window seat, n-th row right window seat. [Image] The seating for n = 9 and m = 36. 

You are given the values n and m. Output m numbers from 1 to m, the order in which the passengers will get off the bus.


-----Input-----

The only line contains two integers, n and m (1 ≤ n ≤ 100, 1 ≤ m ≤ 4n) — the number of pairs of rows and the number of passengers.


-----Output-----

Print m distinct integers from 1 to m — the order in which the passengers will get off the bus.


-----Examples-----
Input
2 7

Output
5 1 6 2 7 3 4

Input
9 36

Output
19 1 20 2 21 3 22 4 23 5 24 6 25 7 26 8 27 9 28 10 29 11 30 12 31 13 32 14 33 15 34 16 35 17 36 18
"""

def calculate_passenger_exit_order(n, m):
    # Initialize the bus seating arrangement
    bus = [[[0 for _ in range(n)] for _ in range(2)] for _ in range(2)]
    
    # Fill the bus with passengers
    passenger_count = 0
    for i in range(1, m + 1):
        passenger_count += 1
        if passenger_count <= 2 * n:
            if passenger_count % 2 != 0:
                bus[0][0][(passenger_count - 1) // 2] = i
            else:
                bus[-1][-1][passenger_count // 2 - 1] = i
        elif passenger_count % 2 != 0:
            bus[0][-1][(passenger_count - 2 * n - 1) // 2] = i
        else:
            bus[-1][0][(passenger_count - 2 * n) // 2 - 1] = i
    
    # Define the order of exit
    indices = [[0, -1], [0, 0], [-1, 0], [-1, -1]]
    exit_order = []
    for i in range(n):
        for k in indices:
            if bus[k[0]][k[1]][i] != 0:
                exit_order.append(bus[k[0]][k[1]][i])
    
    return exit_order