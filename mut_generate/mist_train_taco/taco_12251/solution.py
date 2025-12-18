"""
QUESTION:
There is a hotel with the following accommodation fee:
 - X yen (the currency of Japan) per night, for the first K nights
 - Y yen per night, for the (K+1)-th and subsequent nights
Tak is staying at this hotel for N consecutive nights.
Find his total accommodation fee.

-----Constraints-----
 - 1 \leq N, K \leq 10000
 - 1 \leq Y < X \leq 10000
 - N,\,K,\,X,\,Y are integers.

-----Input-----
The input is given from Standard Input in the following format:
N
K
X
Y

-----Output-----
Print Tak's total accommodation fee.

-----Sample Input-----
5
3
10000
9000

-----Sample Output-----
48000

The accommodation fee is as follows:
 - 10000 yen for the 1-st night
 - 10000 yen for the 2-nd night
 - 10000 yen for the 3-rd night
 - 9000 yen for the 4-th night
 - 9000 yen for the 5-th night
Thus, the total is 48000 yen.
"""

def calculate_total_accommodation_fee(N, K, X, Y):
    """
    Calculate the total accommodation fee for Tak staying at the hotel for N nights.

    Parameters:
    - N (int): Number of nights Tak stays at the hotel.
    - K (int): Number of nights with the initial fee.
    - X (int): Fee per night for the first K nights.
    - Y (int): Fee per night for the nights after the first K nights.

    Returns:
    - int: The total accommodation fee.
    """
    return min(N, K) * X + max(N - K, 0) * Y