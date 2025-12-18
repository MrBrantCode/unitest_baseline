"""
QUESTION:
There is the word heuristics. It's a relatively simple approach that usually works, although there is no guarantee that it will work. The world is full of heuristics because it is simple and powerful.

Some examples of heuristics include: In an anime program, the popularity of a character is proportional to the total appearance time in the main part of the anime. Certainly this seems to hold true in many cases. However, it seems that I belong to the minority. Only characters with light shadows and mobs that glimpse in the background look cute.

It doesn't matter what other people think of your favorite character. Unfortunately, there are circumstances that cannot be said. Related products, figures and character song CDs, tend to be released with priority from popular characters. Although it is a commercial choice, fans of unpopular characters have a narrow shoulder.

Therefore, what is important is the popularity vote held by the production company of the anime program. Whatever the actual popularity, getting a lot of votes here opens the door to related products. You have to collect votes by any means.

For strict voting, you will be given one vote for each purchase of a related product. Whether or not this mechanism should be called strict is now being debated, but anyway I got the right to vote for L votes. There are a total of N characters to be voted on, and related products of K characters who have won more votes (in the case of the same vote, in dictionary order of names) will be planned. I have M characters in all, and I want to put as many characters as possible in the top K.

I first predicted how many votes each character would get (it's not difficult, I just assumed that a character's popularity is proportional to the sum of its appearance times). Given that this prediction is correct, who and how much should I cast this L-vote to ensure that more related products of my favorite characters are released?



Input

The input consists of multiple cases. Each case is given in the following format.


N M K L
name0 x0
..
..
..
nameN-1 xN-1
fav0
..
..
..
favM-1


The meanings of N, M, K, and L are as described in the problem statement.
namei is the name of the character and xi is the total number of votes for the i-th character.
favi represents the name of the character you like. These names are always different and are always included in the character's name input.


The end of the input is given by a line consisting of N = 0, M = 0, K = 0, and L = 0.


In addition, each value satisfies the following conditions
1 ≤ N ≤ 100,000
1 ≤ M ≤ N
1 ≤ K ≤ N
1 ≤ L ≤ 100,000,000
0 ≤ xi ≤ 100,000,000
namei contains only the alphabet and is 10 characters or less in length.

The number of test cases does not exceed 150.
It is also guaranteed that the number of cases where 20,000 ≤ N does not exceed 20.


Judge data is large, so it is recommended to use fast input.

Output

Output in one line how many of the M characters can be included in the top K.

Example

Input

4 1 3 4
yskwcnt 16
akzakr 7
tsnukk 12
fnmyi 13
akzakr
4 1 3 5
akzakr 7
tsnukk 12
fnmyi 13
yskwcnt 16
akzakr
4 2 2 1
akzakr 4
tsnukk 6
yskwcnt 6
fnmyi 12
akzakr
fnmyi
5 2 3 28
knmmdk 6
skrkyk 14
tmemm 14
akmhmr 15
mksyk 25
knmmdk
skrkyk
5 2 3 11
tmemm 12
skrkyk 18
knmmdk 21
mksyk 23
akmhmr 42
skrkyk
tmemm
14 5 10 38
iormns 19
hbkgnh 23
yyitktk 31
rtkakzk 36
mmftm 43
ykhhgwr 65
hrkamm 66
ktrotns 67
mktkkc 68
mkhsi 69
azsmur 73
tknsj 73
amftm 81
chyksrg 88
mkhsi
hbkgnh
mktkkc
yyitktk
tknsj
14 5 10 38
mktkkc 24
rtkakzk 25
ykhhgwr 25
hrkamm 27
amftm 37
iormns 38
tknsj 38
yyitktk 39
hbkgnh 53
mmftm 53
chyksrg 63
ktrotns 63
azsmur 65
mkhsi 76
mkhsi
hbkgnh
mktkkc
yyitktk
tknsj
0 0 0 0


Output

0
1
1
2
1
4
5
"""

def calculate_max_fav_characters(n, m, k, l, character_votes, favorite_characters):
    # Sort characters by votes in descending order, and by name in ascending order in case of tie
    ranking = sorted(character_votes, key=lambda x: (-x[1], x[0]))
    
    # Separate favorite and non-favorite characters
    favs_x = {}
    not_favs_x = {}
    for name, votes in ranking:
        if name in favorite_characters:
            favs_x[name] = votes
        else:
            not_favs_x[name] = votes
    
    # Sort favorite and non-favorite characters by votes and name
    favs_ranking = sorted(favs_x.items(), key=lambda x: (-x[1], x[0]))
    not_favs_ranking = sorted(not_favs_x.items(), key=lambda x: (-x[1], x[0]))
    
    # Lengths of favorite and non-favorite rankings
    favs_length = len(favs_ranking)
    not_favs_length = len(not_favs_ranking)
    
    def check(num):
        not_favs_num = k - num
        if num > favs_length:
            return False
        if not_favs_num >= not_favs_length:
            return True
        target_name, target_x = not_favs_ranking[not_favs_num]
        need = 0
        for name, x in favs_ranking[:num]:
            if target_name > name:
                if target_x <= x:
                    continue
                else:
                    need += target_x - x
            elif target_x < x:
                continue
            else:
                need += target_x - x + 1
        return need <= l
    
    # Binary search to find the maximum number of favorite characters in top k
    left = 0
    right = min(k, favs_length) + 1
    while True:
        if right <= left + 1:
            break
        center = (left + right) // 2
        if check(center):
            left = center
        else:
            right = center
    
    return left