"""
QUESTION:
Vasya has started watching football games. He has learned that for some fouls the players receive yellow cards, and for some fouls they receive red cards. A player who receives the second yellow card automatically receives a red card.

Vasya is watching a recorded football match now and makes notes of all the fouls that he would give a card for. Help Vasya determine all the moments in time when players would be given red cards if Vasya were the judge. For each player, Vasya wants to know only the first moment of time when he would receive a red card from Vasya.


-----Input-----

The first line contains the name of the team playing at home. The second line contains the name of the team playing away. Both lines are not empty. The lengths of both lines do not exceed 20. Each line contains only of large English letters. The names of the teams are distinct.

Next follows number n (1 ≤ n ≤ 90) — the number of fouls. 

Each of the following n lines contains information about a foul in the following form:   first goes number t (1 ≤ t ≤ 90) — the minute when the foul occurs;  then goes letter "h" or letter "a" — if the letter is "h", then the card was given to a home team player, otherwise the card was given to an away team player;  then goes the player's number m (1 ≤ m ≤ 99);  then goes letter "y" or letter "r" — if the letter is "y", that means that the yellow card was given, otherwise the red card was given. 

The players from different teams can have the same number. The players within one team have distinct numbers. The fouls go chronologically, no two fouls happened at the same minute.


-----Output-----

For each event when a player received his first red card in a chronological order print a string containing the following information:  The name of the team to which the player belongs;  the player's number in his team;  the minute when he received the card. 

If no player received a card, then you do not need to print anything.

It is possible case that the program will not print anything to the output (if there were no red cards).


-----Examples-----
Input
MC
CSKA
9
28 a 3 y
62 h 25 y
66 h 42 y
70 h 25 y
77 a 4 y
79 a 25 y
82 h 42 r
89 h 16 y
90 a 13 r

Output
MC 25 70
MC 42 82
CSKA 13 90
"""

def determine_red_cards(team_home, team_away, fouls):
    st1 = set()
    st2 = set()
    d = defaultdict(list)
    for i in range(1, 100):
        d[i] = [0, team_home]
    d2 = defaultdict(list)
    for i in range(1, 100):
        d2[i] = [0, team_away]
    res = []
    
    for foul in fouls:
        t, s, num, c = foul
        if (s == 'h' and num not in st1) or (s == 'a' and num not in st2):
            if c == 'r':
                if s == 'h':
                    res.append((team_home, num, t))
                    st1.add(num)
                else:
                    res.append((team_away, num, t))
                    st2.add(num)
            elif s == 'h':
                if d[num][0] == 0:
                    d[num][0] = 1
                else:
                    res.append((team_home, num, t))
                    st1.add(num)
            elif d2[num][0] == 0:
                d2[num][0] = 1
            else:
                res.append((team_away, num, t))
                st2.add(num)
    
    return res