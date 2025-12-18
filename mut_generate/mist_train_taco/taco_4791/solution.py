"""
QUESTION:
Two friends David and Rojer were preparing for their weekly class-test.
The are preparing for the math test, but because of continuously adding big integers and solving equations they got exhausted. They decided to take break and play a game. They play a game which will help them in both(for having fun and will also help to prepare for math test).
There are N words and they have to find RESULT with the help of these words (just like they have N integers and they have to find integer RESULT=sum of N integers) . Since they are playing this game for the first time! They are not too good in this. Help them in finding weather their RESULT is correct or not.   
NOTE:- Total number of unique characters in N words are not greater than 10. All input words and RESULT are in UPPER-CASE only!
Refer Here for how to add numbers : https://en.wikipedia.org/wiki/Verbal_arithmetic

-----Input:-----
- First line consist of an integer N (total number of words).
- Next N line contains words with which they have to find RESULT.
- Last line consist of the RESULT they found.

-----Output:-----
If RESULT is correct print true else print false.

-----Sample Input:-----
3

THIS

IS

TOO

FUNNY  

-----Sample Output:-----
true

-----Constraints-----
- $2 \leq N \leq 10$
- $1 \leq Length of The word \leq 10$
- $1 \leq Length of The Result \leq 11$
"""

def is_result_correct(words, result):
    (LW, LR, F, ML, AW, V, LMap) = (len(words), len(result), set([w[0] for w in words + [result]]), max(map(len, words + [result])), words + [result], set(), {})
    if LR < ML:
        return False

    def dfs(d, i, c):
        if d == ML:
            return c == 0
        if i == len(words) + 1:
            s = sum((LMap[w[-d - 1]] if d < len(w) else 0 for w in words)) + c
            return dfs(d + 1, 0, s // 10) if s % 10 == LMap[result[-d - 1]] else False
        if i < LW and d >= len(words[i]):
            return dfs(d, i + 1, c)
        ch = AW[i][-d - 1]
        if ch in LMap:
            return dfs(d, i + 1, c)
        for x in range(ch in F, 10):
            if x not in V:
                (LMap[ch], _) = (x, V.add(x))
                if dfs(d, i + 1, c):
                    return True
                V.remove(LMap.pop(ch))
        return False

    return dfs(0, 0, 0)