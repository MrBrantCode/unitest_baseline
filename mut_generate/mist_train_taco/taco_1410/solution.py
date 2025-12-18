"""
QUESTION:
Once upon a time, a king and a few of his soldiers were  caught by an enemy king in a war. 

He puts them in a circle. The first man in the circle has to kill the second man, the third man has to kill the fourth, fifth man to kill the sixth and so on. When the circle is completed, the remaining people have to form a circle and the process has to repeat. The last man standing will be set free.

If the king has to be set free, which position must he take? For any given N number of people, write a program to find the position that the king has to take.

-----Input-----
Any positive integer in the range 1 to 10000.

-----Output-----
A positive integer indicating safest position

-----Example-----
Input:
9

Output:
3
"""

def find_safe_position(n: int) -> int:
    arr = list(range(1, n + 1))
    c = 0
    i = 0
    f = 0
    
    while c < n - 1:
        if arr[i % n] != -1 and f:
            arr[i % n] = -1
            c += 1
            f = 0
        if arr[i % n] != -1:
            f = 1
        i += 1
    
    for i in range(n):
        if arr[i] != -1:
            return arr[i]

# Example usage:
# print(find_safe_position(9))  # Output: 3