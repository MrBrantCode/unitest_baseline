"""
QUESTION:
Bob loves everything sweet. His favorite chocolate bar consists of pieces, each piece may contain a nut. Bob wants to break the bar of chocolate into multiple pieces so that each part would contain exactly one nut and any break line goes between two adjacent pieces.

You are asked to calculate the number of ways he can do it. Two ways to break chocolate are considered distinct if one of them contains a break between some two adjacent pieces and the other one doesn't. 

Please note, that if Bob doesn't make any breaks, all the bar will form one piece and it still has to have exactly one nut.


-----Input-----

The first line of the input contains integer n (1 ≤ n ≤ 100) — the number of pieces in the chocolate bar.

The second line contains n integers a_{i} (0 ≤ a_{i} ≤ 1), where 0 represents a piece without the nut and 1 stands for a piece with the nut.


-----Output-----

Print the number of ways to break the chocolate into multiple parts so that each part would contain exactly one nut.


-----Examples-----
Input
3
0 1 0

Output
1

Input
5
1 0 1 0 1

Output
4



-----Note-----

In the first sample there is exactly one nut, so the number of ways equals 1 — Bob shouldn't make any breaks.

In the second sample you can break the bar in four ways:

10|10|1

1|010|1

10|1|01

1|01|01
"""

def count_ways_to_break_chocolate(n, pieces):
    # Convert the list of integers to a list of strings for easier manipulation
    pieces_str = [str(piece) for piece in pieces]
    
    # Check if there is at least one nut in the chocolate bar
    if '1' not in pieces_str:
        return 0
    
    # Trim the pieces to only include the first and last nut
    start_index = pieces_str.index('1')
    end_index = n - 1 - pieces_str[::-1].index('1')
    trimmed_pieces = pieces_str[start_index:end_index + 1]
    
    # Initialize the result and step counter
    result = 1
    step = 0
    
    # Iterate through the trimmed pieces to calculate the number of ways
    for piece in trimmed_pieces:
        step += 1
        if piece == '1':
            result *= step
            step = 0
    
    return result