"""
QUESTION:
Skier rides on a snowy field. Its movements can be described by a string of characters 'S', 'N', 'W', 'E' (which correspond to $1$ meter movement in the south, north, west or east direction respectively).

It is known that if he moves along a previously unvisited segment of a path (i.e. this segment of the path is visited the first time), then the time of such movement is $5$ seconds. If he rolls along previously visited segment of a path (i.e., this segment of the path has been covered by his path before), then it takes $1$ second.

Find the skier's time to roll all the path.


-----Input-----

The first line contains an integer $t$ ($1 \le t \le 10^4$) — the number of test cases in the input. Then $t$ test cases follow.

Each set is given by one nonempty string of the characters 'S', 'N', 'W', 'E'. The length of the string does not exceed $10^5$ characters.

The sum of the lengths of $t$ given lines over all test cases in the input does not exceed $10^5$.


-----Output-----

For each test case, print the desired path time in seconds.


-----Example-----
Input
5
NNN
NS
WWEN
WWEE
NWNWS

Output
15
6
16
12
25
"""

def calculate_skier_time(movements: str) -> int:
    visited_segments = set()
    time_taken = 0
    x, y = 0, 0
    
    for move in movements:
        start_pos = (x, y)
        if move == 'N':
            y += 1
        elif move == 'S':
            y -= 1
        elif move == 'E':
            x += 1
        elif move == 'W':
            x -= 1
        
        end_pos = (x, y)
        segment = (start_pos, end_pos)
        reverse_segment = (end_pos, start_pos)
        
        if segment in visited_segments or reverse_segment in visited_segments:
            time_taken += 1
        else:
            time_taken += 5
            visited_segments.add(segment)
            visited_segments.add(reverse_segment)
    
    return time_taken