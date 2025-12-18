"""
QUESTION:
Teddy and Tracy like to play a game based on strings. The game is as follows. Initially, Tracy writes a long random string on a whiteboard. Then, each player starting with Teddy makes turn alternately. Each turn, the player must erase a contiguous substring that exists in the dictionary. The dictionary consists of N words.

Of course, the player that can't erase any substring in his turn loses the game, and the other player is declared the winner.

Note that after a substring R is erased, the remaining substring becomes separated, i.e. they cannot erase a word that occurs partially to the left of R and partially to the right of R.

Determine the winner of the game, assuming that both players play optimally.

------ Input ------ 

The first line contains a single integer T, the number of test cases. T test cases follow. The first line of each testcase contains a string S, the string Tracy writes on the whiteboard. The next line contains a single integer N. N lines follow. The i-th line contains a single string w_{i}, the i-th word in the dictionary.

------ Output ------ 

For each test case, output a single line containing the name of the winner of the game.

------ Constraints ------ 

$1 ≤ T ≤ 5$
$1 ≤ N ≤ 30$
$1 ≤ |S| ≤ 30$
$1 ≤ |w_{i}| ≤ 30$
$S and w_{i} contain only characters 'a'-'z'$

----- Sample Input 1 ------ 
3
codechef
2
code
chef
foo
1
bar
mississippi
4
ssissi
mippi
mi
ppi
----- Sample Output 1 ------ 
Tracy
Tracy
Teddy
"""

def determine_winner(S, N, words):
    def grundy(g):
        if g in gdic:
            return gdic[g]
        lg = len(g)
        subg = set()
        for (ln, w) in words:
            pos = g.find(w)
            while pos >= 0:
                gpre = grundy(g[:pos])
                gpost = grundy(g[pos + ln:])
                subg.add(gpre ^ gpost)
                pos = g.find(w, pos + 1)
        if len(subg) == 0:
            gdic[g] = 0
        else:
            mex = 0
            while mex in subg:
                mex += 1
            gdic[g] = mex
        return gdic[g]
    
    wordset = set(words)
    words = [(len(w), w) for w in wordset]
    gdic = {'': 0}
    return 'Teddy' if grundy(S) > 0 else 'Tracy'