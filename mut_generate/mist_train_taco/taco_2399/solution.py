"""
QUESTION:
Sometimes Mister B has free evenings when he doesn't know what to do. Fortunately, Mister B found a new game, where the player can play against aliens.

All characters in this game are lowercase English letters. There are two players: Mister B and his competitor.

Initially the players have a string s consisting of the first a English letters in alphabetical order (for example, if a = 5, then s equals to "abcde").

The players take turns appending letters to string s. Mister B moves first.

Mister B must append exactly b letters on each his move. He can arbitrary choose these letters. His opponent adds exactly a letters on each move.

Mister B quickly understood that his opponent was just a computer that used a simple algorithm. The computer on each turn considers the suffix of string s of length a and generates a string t of length a such that all letters in the string t are distinct and don't appear in the considered suffix. From multiple variants of t lexicographically minimal is chosen (if a = 4 and the suffix is "bfdd", the computer chooses string t equal to "aceg"). After that the chosen string t is appended to the end of s.

Mister B soon found the game boring and came up with the following question: what can be the minimum possible number of different letters in string s on the segment between positions l and r, inclusive. Letters of string s are numerated starting from 1.


-----Input-----

First and only line contains four space-separated integers: a, b, l and r (1 ≤ a, b ≤ 12, 1 ≤ l ≤ r ≤ 10^9) — the numbers of letters each player appends and the bounds of the segment.


-----Output-----

Print one integer — the minimum possible number of different letters in the segment from position l to position r, inclusive, in string s.


-----Examples-----
Input
1 1 1 8

Output
2
Input
4 2 2 6

Output
3
Input
3 7 4 6

Output
1


-----Note-----

In the first sample test one of optimal strategies generate string s = "abababab...", that's why answer is 2.

In the second sample test string s = "abcdbcaefg..." can be obtained, chosen segment will look like "bcdbc", that's why answer is 3.

In the third sample test string s = "abczzzacad..." can be obtained, chosen, segment will look like "zzz", that's why answer is 1.
"""

def min_different_letters(a, b, l, r):
    qL = (l - 1) // (2 * a + 2 * b)
    rL = (l - 1) % (2 * a + 2 * b) + 1
    qR = (r - 1) // (2 * a + 2 * b)
    rR = (r - 1) % (2 * a + 2 * b) + 1
    
    if qL == qR:
        if a < rL <= a + b and a < rR <= a + b:
            return 1
        if 2 * a + b < rL and 2 * a + b < rR:
            return 1
        if 1 <= rL <= a and 1 <= rR <= a:
            return rR - rL + 1
        if a + b < rL <= 2 * a + b and a + b < rR <= 2 * a + b:
            return rR - rL + 1
        if 1 <= rL <= a + b and 1 <= rR <= a + b:
            return a - rL + 1
        if a + b < rL and a + b < rR:
            return 2 * a + b - rL + 1
        if a < rL <= a + b and a + b < rR <= 2 * a + b:
            return 1 + rR - (a + b)
        if a < rL <= a + b and 2 * a + b < rR:
            return 1 + a
        if 1 <= rL <= a and a + b < rR <= 2 * a + b:
            ans = a - rL + 1 + max(rR - (a + b + b), 0) + min(b, rR) - max(min(rR, b) - rL + 1, 0)
            return ans
        if 1 <= rL <= a and 2 * a + b < rR:
            return a - rL + 1 + a - max(b - rL + 1, 0)
    elif qL == qR - 1:
        newL = qL * (2 * a + 2 * b) + 1
        newR = (qR + 1) * (2 * a + 2 * b)
        if 1 <= rL <= a + b and a + b + 1 <= rR:
            return a + max(a - b, 0) + int(a <= b)
        if a + b + 1 <= rL <= 2 * (a + b) and 2 * a + 2 * b + 1 <= rR <= a + b:
            return min_different_letters(a, b, l - (a + b), r - (a + b))
        if 1 <= rL <= a and 1 <= rR <= a:
            return a + max(a - b, 0) + int(a <= b) + rR - max(rR - rL + 1, 0)
        if 1 <= rL <= a and a + 1 <= rR <= a + b:
            return a + max(a - b, 0) + int(a <= b)
        if a + 1 <= rL <= a + b and 1 <= rR <= a:
            return 1 + a
        if a + 1 <= rL <= a + b and a + 1 <= rR <= a + b:
            return 1 + a + max(a - b, 0)
        return min_different_letters(a, b, l - (a + b), r - (a + b))
    else:
        return a + max(a - b, 0) + int(a <= b)