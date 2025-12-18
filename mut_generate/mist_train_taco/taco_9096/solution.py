"""
QUESTION:
Vasya has a pack of 54 cards (52 standard cards and 2 distinct jokers). That is all he has at the moment. Not to die from boredom, Vasya plays Solitaire with them.

Vasya lays out nm cards as a rectangle n × m. If there are jokers among them, then Vasya should change them with some of the rest of 54 - nm cards (which are not layed out) so that there were no jokers left. Vasya can pick the cards to replace the jokers arbitrarily. Remember, that each card presents in pack exactly once (i. e. in a single copy). Vasya tries to perform the replacements so that the solitaire was solved.

Vasya thinks that the solitaire is solved if after the jokers are replaced, there exist two non-overlapping squares 3 × 3, inside each of which all the cards either have the same suit, or pairwise different ranks.

Determine by the initial position whether the solitaire can be solved or not. If it can be solved, show the way in which it is possible.

Input

The first line contains integers n and m (3 ≤ n, m ≤ 17, n × m ≤ 52). Next n lines contain m words each. Each word consists of two letters. The jokers are defined as "J1" and "J2" correspondingly. For the rest of the cards, the first letter stands for the rank and the second one — for the suit. The possible ranks are: "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K" and "A". The possible suits are: "C", "D", "H" and "S". All the cards are different.

Output

If the Solitaire can be solved, print on the first line "Solution exists." without the quotes. On the second line print in what way the jokers can be replaced. Three variants are possible:

  * "There are no jokers.", if there are no jokers in the input data.
  * "Replace Jx with y.", if there is one joker. x is its number, and y is the card it should be replaced with.
  * "Replace J1 with x and J2 with y.", if both jokers are present in the input data. x and y here represent distinct cards with which one should replace the first and the second jokers correspondingly.



On the third line print the coordinates of the upper left corner of the first square 3 × 3 in the format "Put the first square to (r, c).", where r and c are the row and the column correspondingly. In the same manner print on the fourth line the coordinates of the second square 3 × 3 in the format "Put the second square to (r, c).".

If there are several solutions to that problem, print any of them.

If there are no solutions, print of the single line "No solution." without the quotes.

See the samples to understand the output format better.

Examples

Input

4 6
2S 3S 4S 7S 8S AS
5H 6H 7H 5S TC AC
8H 9H TH 7C 8C 9C
2D 2C 3C 4C 5C 6C


Output

No solution.

Input

4 6
2S 3S 4S 7S 8S AS
5H 6H 7H J1 TC AC
8H 9H TH 7C 8C 9C
2D 2C 3C 4C 5C 6C


Output

Solution exists.
Replace J1 with 2H.
Put the first square to (1, 1).
Put the second square to (2, 4).


Input

4 6
2S 3S 4S 7S 8S AS
5H 6H 7H QC TC AC
8H 9H TH 7C 8C 9C
2D 2C 3C 4C 5C 6C


Output

Solution exists.
There are no jokers.
Put the first square to (1, 1).
Put the second square to (2, 4).

Note

The pretests cover all the possible output formats.
"""

def solve_solitaire(n, m, board):
    ranks = '23456789TJQKA'
    suits = 'CDHS'
    p = [r + s for r in ranks for s in suits]
    j1, j2 = False, False
    j1v, j2v = None, None
    n0, m0, n1, m1 = None, None, None, None

    for r in board:
        for c in r:
            if c == 'J1':
                j1 = True
            elif c == 'J2':
                j2 = True
            else:
                p.remove(c)

    def valid(n, m):
        r = set()
        s = set()
        for ni in range(n, n + 3):
            for mi in range(m, m + 3):
                c = board[ni][mi]
                if c == 'J1':
                    c = j1v
                if c == 'J2':
                    c = j2v
                r.add(c[0])
                s.add(c[1])
        return len(r) == 9 or len(s) == 1

    def solve():
        nonlocal j1v, j2v, n0, m0, n1, m1
        for j1v in p:
            for j2v in p:
                if j1v == j2v:
                    continue
                for n0 in range(n - 2):
                    for m0 in range(m - 2):
                        if not valid(n0, m0):
                            continue
                        for n1 in range(n - 2):
                            for m1 in range(m - 2):
                                if n0 + 2 < n1 or n1 + 2 < n0 or m0 + 2 < m1 or (m1 + 2 < m0):
                                    if valid(n1, m1):
                                        return True
        return False

    solution_exists = solve()
    result = {
        'solution_exists': solution_exists,
        'j1_replacement': j1v if j1 else None,
        'j2_replacement': j2v if j2 else None,
        'first_square': (n0 + 1, m0 + 1) if solution_exists else None,
        'second_square': (n1 + 1, m1 + 1) if solution_exists else None
    }
    return result