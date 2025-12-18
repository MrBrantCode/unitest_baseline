"""
QUESTION:
Write a function `calculateTime(keyboard: str, word: str) -> int` to calculate the time it takes to type a string `word` on a special keyboard with all keys in a single row and a shift key. The keyboard layout is given as a string `keyboard` of length 52, where the first 26 characters are lowercase and the next 26 are uppercase. The function should return the total time taken to type the `word`, where the time taken to move from index `i` to index `j` is `|i - j|` and pressing the shift key takes 1 unit of time. The constraints are `keyboard.length == 52`, `keyboard` contains each English lowercase and uppercase letter exactly once, `1 <= word.length <= 104`, and `word[i]` is an English lowercase or uppercase letter.
"""

def calculateTime(keyboard: str, word: str) -> int:
    pos = {char: idx for idx, char in enumerate(keyboard)}
    time = prev = 0
    for char in word:
        current = pos[char]
        if prev <=26 and  current >= 26:
            time += abs(current // 26 - prev // 26) + abs(current % 26 - prev % 26)
        else:
            time += abs(current - prev)
        prev = current
    return time