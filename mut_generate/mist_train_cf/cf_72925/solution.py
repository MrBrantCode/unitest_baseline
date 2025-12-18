"""
QUESTION:
Write a function `minimumDistance(word: str) -> int` that calculates the minimum total distance to type the given string `word` using two fingers, with the constraints that the first finger can only type the letters 'A', 'E', 'I', 'M', 'Q', 'U', 'Y', the second finger can only type the letters 'B', 'F', 'J', 'N', 'R', 'V', 'Z', and the remaining letters can be typed by either finger. The distance between coordinates (x1,y1) and (x2,y2) is |x1 - x2| + |y1 - y2|. The initial positions of the two fingers are considered free and do not count towards the total distance.

Assume that `2 <= word.length <= 300` and each `word[i]` is an English uppercase letter.
"""

def minimumDistance(word: str) -> int:
    def get_cost(pos1: int, pos2: int) -> int:
        x1, y1 = divmod(pos1, 6)
        x2, y2 = divmod(pos2, 6)
        return abs(x1 - x2) + abs(y1 - y2)
    
    dp1, dp2, dp0 = [0]*26, [0]*26, [0]*26
    for i in range(len(word) - 1, -1, -1):
        pos = ord(word[i]) - 65
        for b in range(26):
            dp2[b] = min(get_cost(pos, b) + dp0[pos], get_cost(pos, b) + dp1[b])
        dp1, dp0 = dp2, dp1
    return min(dp0)