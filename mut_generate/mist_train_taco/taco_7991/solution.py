"""
QUESTION:
You are the planning manager of an animation production company. What animation production companies produce these days is not limited to animation itself. Related products, such as figures of characters and character song CDs, are also important sources of revenue. How much this profit can be increased depends solely on you, the director of the planning department.

Obviously, these related products are not something that should be released in the dark clouds. This is because it takes a lot of time and budget to develop a product. Even if you release a figure of an anime character, you have to limit it to popular characters that are expected to sell a lot.

One of the means to measure the popularity of a character is popularity voting. You've been planning some popularity polls so far, but it seems that viewers are becoming dissatisfied with the project. There is an urgent need to establish other methods for measuring popularity.

So you made a hypothesis. The popularity of a character is proportional to the total appearance time in the main part of the anime. To test this hypothesis, you decided to write a program that aggregates the appearance times of each character.



Input

The input consists of multiple cases. Each case is given in the following format.


n
name0 m0 d0,0 ... d0, m0-1
name1 m1 d1,0 ... d1, m1-1
..
..
..
namen-1 mn-1 dn-1,0 ... dn-1, mn-1-1



n represents the number of characters.
namei represents the name of the character.
mi represents the type of time the character was shown.
After mi, mi integers di and j are given.
di and j represent the time when the character was shown.
The end of the input is given by a line consisting of n = 0


If only one character appears on the screen at a given time, that character can get n points.
Every time one more character appears at the same time, the points obtained for the character reflected at that time decrease by one.
If n characters are shown at the same time, 1 point will be added to each of n characters.


The input satisfies the following constraints.
2 ≤ n ≤ 20
0 ≤ mi ≤ 30
0 ≤ di, j <30
Di and j are all different for the i-th character.
namei contains only uppercase or lowercase letters and is no longer than 10.

Output

Output the points of the character with the smallest points and their names separated by a single space.
If there are multiple characters with the smallest points, select the person with the smallest name in lexicographical order.

Example

Input

4
akzakr 2 1 8
fnmyi 5 2 3 4 6 9
tsnukk 5 2 3 4 7 9
yskwcnt 6 3 4 7 8 9 10
4
akzakr 1 2
fnmyi 3 10 11 12
tsnukk 2 1 8
yskwcnt 2 1 8
5
knmmdk 2 13 19
akmhmr 4 13 15 19 22
mksyk 6 3 7 12 13 15 19
skrkyk 3 1 4 8
tmemm 3 1 17 24
5
knmmdk 5 5 6 16 18 26
akmhmr 9 3 4 7 11 14 15 17 18 20
mksyk 5 6 13 25 27 28
skrkyk 4 3 16 23 24
tmemm 3 6 12 20
14
hrkamm 6 4 6 8 10 20 22
mkhsi 6 1 10 12 15 22 27
hbkgnh 2 4 9
chyksrg 8 3 4 12 15 16 20 25 28
mktkkc 6 0 1 8 15 17 20
tknsj 6 6 8 18 19 25 26
yyitktk 3 3 12 18
ykhhgwr 5 3 9 10 11 24
amftm 7 2 6 8 12 13 14 17
mmftm 4 6 12 16 18
rtkakzk 3 14 15 21
azsmur 7 1 2 4 12 15 18 20
iormns 2 4 20
ktrotns 6 7 12 14 17 20 25
14
hrkamm 2 4 21
mkhsi 6 2 3 8 11 18 20
hbkgnh 4 4 16 28 29
chyksrg 5 0 3 9 17 22
mktkkc 2 7 18
tknsj 3 3 9 23
yyitktk 3 10 13 25
ykhhgwr 2 18 26
amftm 3 13 18 22
mmftm 4 1 20 24 27
rtkakzk 2 1 10
azsmur 5 2 5 10 14 17
iormns 3 9 15 16
ktrotns 5 7 12 16 17 20
0


Output

7 akzakr
4 akzakr
6 knmmdk
12 tmemm
19 iormns
24 mktkkc
"""

def calculate_popularity_scores(characters):
    if not characters:
        return None, None
    
    # Initialize frequency table and character table
    frequency = [0] * 31
    character_table = []
    
    # Populate frequency table and character table
    for name, appearances in characters:
        character_table.append([0, name, appearances])
        for time in appearances:
            frequency[time] += 1
    
    # Calculate scores for each character
    for i in range(len(character_table)):
        for time in character_table[i][2]:
            character_table[i][0] += len(characters) - frequency[time] + 1
    
    # Sort the character table by score and then by name
    character_table.sort(key=lambda x: (x[0], x[1]))
    
    # Return the character with the minimum score and their name
    min_score, min_name, _ = character_table[0]
    return min_score, min_name