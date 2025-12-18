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

def find_olympiad_year(abbreviations):
    # Precompute the starting years and their corresponding suffixes
    tn = [0] * 10000
    ts = [0] * 10000
    a = 1989
    tn[1] = 1989
    ts[1] = 9
    for i in range(1, 12):
        a = a + 10 ** i
        tn[i + 1] = a
        ts[i + 1] = int(str(a)[-i - 1:])
    
    # Process each abbreviation
    years = []
    for abbreviation in abbreviations:
        y = abbreviation[4:]
        temp = len(y)
        y = int(y)
        year = (y - ts[temp]) % 10 ** temp + tn[temp]
        years.append(year)
    
    return years