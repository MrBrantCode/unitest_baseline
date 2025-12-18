"""
QUESTION:
You have a playlist consisting of $n$ songs. The $i$-th song is characterized by two numbers $t_i$ and $b_i$ — its length and beauty respectively. The pleasure of listening to set of songs is equal to the total length of the songs in the set multiplied by the minimum beauty among them. For example, the pleasure of listening to a set of $3$ songs having lengths $[5, 7, 4]$ and beauty values $[11, 14, 6]$ is equal to $(5 + 7 + 4) \cdot 6 = 96$.

You need to choose at most $k$ songs from your playlist, so the pleasure of listening to the set of these songs them is maximum possible.


-----Input-----

The first line contains two integers $n$ and $k$ ($1 \le k \le n \le 3 \cdot 10^5$) – the number of songs in the playlist and the maximum number of songs you can choose, respectively.

Each of the next $n$ lines contains two integers $t_i$ and $b_i$ ($1 \le t_i, b_i \le 10^6$) — the length and beauty of $i$-th song.


-----Output-----

Print one integer — the maximum pleasure you can get.


-----Examples-----
Input
4 3
4 7
15 1
3 6
6 8

Output
78

Input
5 3
12 31
112 4
100 100
13 55
55 50

Output
10000



-----Note-----

In the first test case we can choose songs ${1, 3, 4}$, so the total pleasure is $(4 + 3 + 6) \cdot 6 = 78$.

In the second test case we can choose song $3$. The total pleasure will be equal to $100 \cdot 100 = 10000$.
"""

import heapq

def max_playlist_pleasure(n, k, songs):
    # Sort songs by beauty in descending order
    songs.sort(key=lambda x: x[1], reverse=True)
    
    max_pleasure = 0
    current_time = 0
    min_heap = []
    
    for t, b in songs:
        # Add the current song's length to the total time
        current_time += t
        # Push the current song's length to the min-heap
        heapq.heappush(min_heap, t)
        
        # If we exceed the maximum number of songs, remove the smallest length
        if len(min_heap) > k:
            current_time -= heapq.heappop(min_heap)
        
        # Calculate the pleasure for the current set of songs
        max_pleasure = max(max_pleasure, current_time * b)
    
    return max_pleasure