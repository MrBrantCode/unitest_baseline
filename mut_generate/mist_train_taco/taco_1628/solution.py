"""
QUESTION:
The development of a text editor is a hard problem. You need to implement an extra module for brackets coloring in text.

Your editor consists of a line with infinite length and cursor, which points to the current character. Please note that it points to only one of the characters (and not between a pair of characters). Thus, it points to an index character. The user can move the cursor left or right one position. If the cursor is already at the first (leftmost) position, then it does not move left.

Initially, the cursor is in the first (leftmost) character.

Also, the user can write a letter or brackets (either (, or )) to the position that the cursor is currently pointing at. A new character always overwrites the old value at that position.

Your editor must check, whether the current line is the correct text. Text is correct if the brackets in them form the correct bracket sequence.

Formally, correct text (CT) must satisfy the following rules:   any line without brackets is CT (the line can contain whitespaces);  If the first character of the string — is (, the last — is ), and all the rest form a CT, then the whole line is a CT;  two consecutively written CT is also CT. 

Examples of correct texts: hello(codeforces), round, ((i)(write))edi(tor)s, ( me). Examples of incorrect texts: hello)oops(, round), ((me).

The user uses special commands to work with your editor. Each command has its symbol, which must be written to execute this command.

The correspondence of commands and characters is as follows:   L — move the cursor one character to the left (remains in place if it already points to the first character);  R — move the cursor one character to the right;  any lowercase Latin letter or bracket (( or )) — write the entered character to the position where the cursor is now. 

For a complete understanding, take a look at the first example and its illustrations in the note below.

You are given a string containing the characters that the user entered. For the brackets coloring module's work, after each command you need to:

  check if the current text in the editor is a correct text;  if it is, print the least number of colors that required, to color all brackets. 

If two pairs of brackets are nested (the first in the second or vice versa), then these pairs of brackets should be painted in different colors. If two pairs of brackets are not nested, then they can be painted in different or the same colors. For example, for the bracket sequence ()(())()() the least number of colors is $2$, and for the bracket sequence (()(()())())(()) — is $3$.

Write a program that prints the minimal number of colors after processing each command.


-----Input-----

The first line contains an integer $n$ ($1 \le n \le 10^6$) — the number of commands. 

The second line contains $s$ — a sequence of commands. The string $s$ consists of $n$ characters. It is guaranteed that all characters in a string are valid commands.


-----Output-----

In a single line print $n$ integers, where the $i$-th number is:

  $-1$ if the line received after processing the first $i$ commands is not valid text,  the minimal number of colors in the case of the correct text. 


-----Examples-----
Input
11
(RaRbR)L)L(

Output
-1 -1 -1 -1 -1 -1 1 1 -1 -1 2 
Input
11
(R)R(R)Ra)c

Output
-1 -1 1 1 -1 -1 1 1 1 -1 1 


-----Note-----

In the first example, the text in the editor will take the following form:

  (

^  (

 ^  (a

 ^  (a

  ^  (ab

  ^  (ab

   ^  (ab)

   ^  (ab)

  ^  (a))

  ^  (a))

 ^  (())

 ^
"""

class SegmentTree:
    def __init__(self, n, arr=[]):
        self.n = n
        self.tsum = [0] * (2 * n)
        self.tmin = [0] * (2 * n)
        self.tmax = [0] * (2 * n)
        if arr:
            for i in range(len(arr)):
                self.tsum[n + i] = arr[i]
            for i in range(len(arr) - 1, 0, -1):
                self.tsum[i] = self.tsum[i << 1] + self.tsum[i << 1 | 1]

    def update(self, p, val):
        p += self.n
        self.tsum[p] = val
        self.tmin[p] = val
        self.tmax[p] = val
        i = p
        while i > 1:
            par = i >> 1
            if i & 1:
                self.tsum[par] = self.tsum[i] + self.tsum[i ^ 1]
                self.tmin[par] = min(self.tmin[i ^ 1], self.tmin[i] + self.tsum[i ^ 1])
                self.tmax[par] = max(self.tmax[i ^ 1], self.tmax[i] + self.tsum[i ^ 1])
            else:
                self.tsum[par] = self.tsum[i] + self.tsum[i ^ 1]
                self.tmin[par] = min(self.tmin[i], self.tmin[i ^ 1] + self.tsum[i])
                self.tmax[par] = max(self.tmax[i], self.tmax[i ^ 1] + self.tsum[i])
            i >>= 1

def bracket_coloring_editor(n, s):
    n = 1048576
    st = SegmentTree(n)
    maxit = -1
    currentit = 0
    output = []
    for c in s:
        if c == 'L':
            currentit = max(0, currentit - 1)
        elif c == 'R':
            currentit += 1
        else:
            maxit = max(maxit, currentit)
            if c == '(':
                st.update(currentit, 1)
            elif c == ')':
                st.update(currentit, -1)
            else:
                st.update(currentit, 0)
        vmax = st.tmax[1]
        vmin = st.tmin[1]
        vsum = st.tsum[1]
        if vmin >= 0 and vsum == 0:
            output.append(vmax)
        else:
            output.append(-1)
    return output