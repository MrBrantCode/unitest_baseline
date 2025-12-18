"""
QUESTION:
International Abbreviation Olympiad takes place annually starting from 1989. Each year the competition receives an abbreviation of form IAO'y, where y stands for some number of consequent last digits of the current year. Organizers always pick an abbreviation with non-empty string y that has never been used before. Among all such valid abbreviations they choose the shortest one and announce it to be the abbreviation of this year's competition.

For example, the first three Olympiads (years 1989, 1990 and 1991, respectively) received the abbreviations IAO'9, IAO'0 and IAO'1, while the competition in 2015 received an abbreviation IAO'15, as IAO'5 has been already used in 1995.

You are given a list of abbreviations. For each of them determine the year it stands for.

Input

The first line of the input contains a single integer n (1 ≤ n ≤ 1000) — the number of abbreviations to process. 

Then n lines follow, each containing a single abbreviation. It's guaranteed that each abbreviation contains at most nine digits.

Output

For each abbreviation given in the input, find the year of the corresponding Olympiad.

Examples

Input

5
IAO'15
IAO'2015
IAO'1
IAO'9
IAO'0


Output

2015
12015
1991
1989
1990


Input

4
IAO'9
IAO'99
IAO'999
IAO'9999


Output

1989
1999
2999
9999
"""

def determine_olympiad_year(abbreviations):
    def get_year(s):
        dic = {'9': '1989', '0': '1990', '1': '1991', '2': '1992', '3': '1993', '4': '1994', '5': '1995', '6': '1996', '7': '1997', '8': '1998'}
        length = len(s)
        if len(s) == 1:
            return dic[s]
        pos = [s]
        pre = 1
        if s[0] == '0' or len(s) < 4 or (len(s) == 4 and int(s) < 1989):
            pos = []
        count = 0
        while count < length:
            if int(str(pre) + s) >= 1989:
                pos.append(str(pre) + s)
                count += 1
            pre += 1
        for i in range(1, length):
            year = get_year(s[i:])
            try:
                pos.remove(year)
            except ValueError:
                pass
        return pos[0]
    
    results = []
    for abb in abbreviations:
        year_str = get_year(abb[4:])
        results.append(int(year_str))
    
    return results