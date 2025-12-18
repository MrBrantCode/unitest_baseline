"""
QUESTION:
Write a function `minimumDistance(word: str) -> int` that calculates the minimum total movement cost for typing a word on an alphabet circle where each letter is assigned to a unique position on the circle. The circle consists of 26 positions arranged in a 6x6 grid, with positions numbered from 0 to 25. The movement cost between two positions is the Manhattan distance between them (i.e., the sum of the absolute differences of their x and y coordinates). The function should return the minimum total movement cost for typing the word. 

The alphabet positions on the circle are assumed to be numbered as follows: 
- A is at position 0 (0, 0)
- B is at position 1 (0, 1)
- C is at position 2 (0, 2)
- ...
- Z is at position 25 (5, 5) 

Note that the word only contains uppercase English letters.
"""

def minimumDistance(word: str) -> int:
    def get_cost(pos1: int, pos2: int) -> int:
        x1, y1 = divmod(pos1, 6)
        x2, y2 = divmod(pos2, 6)
        return abs(x1 - x2) + abs(y1 - y2)

    dp1, dp2, dp0 = ([0]*26, [0]*26, [0]*26)
    for i in range(len(word) - 1, -1, -1):
        pos = ord(word[i]) - 65
        for b in range(26):
            dp2[b] = min(get_cost(pos, b) + dp0[b], get_cost(pos, b) + dp1[b])
        dp1, dp0 = dp2, dp1
    return min(dp0)