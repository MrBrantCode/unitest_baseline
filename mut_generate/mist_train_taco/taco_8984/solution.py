"""
QUESTION:
N friends of Takahashi has come to a theme park.
To ride the most popular roller coaster in the park, you must be at least K centimeters tall.
The i-th friend is h_i centimeters tall.
How many of the Takahashi's friends can ride the roller coaster?

-----Constraints-----
 -  1 \le N \le 10^5 
 -  1 \le K \le 500 
 -  1 \le h_i \le 500
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N K
h_1 h_2 \ldots h_N

-----Output-----
Print the number of people among the Takahashi's friends who can ride the roller coaster.

-----Sample Input-----
4 150
150 140 100 200

-----Sample Output-----
2

Two of them can ride the roller coaster: the first and fourth friends.
"""

def count_friends_who_can_ride(N, K, heights):
    """
    Counts the number of friends who can ride the roller coaster based on their heights.

    Parameters:
    - N (int): The number of friends.
    - K (int): The minimum height required to ride the roller coaster.
    - heights (list of int): A list of integers representing the heights of the friends.

    Returns:
    - int: The number of friends who can ride the roller coaster.
    """
    return sum(1 for height in heights if height >= K)