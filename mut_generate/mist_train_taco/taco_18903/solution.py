"""
QUESTION:
Once little Vasya read an article in a magazine on how to make beautiful handmade garland from colored paper. Vasya immediately went to the store and bought n colored sheets of paper, the area of each sheet is 1 square meter.

The garland must consist of exactly m pieces of colored paper of arbitrary area, each piece should be of a certain color. To make the garland, Vasya can arbitrarily cut his existing colored sheets into pieces. Vasya is not obliged to use all the sheets to make the garland.

Vasya wants the garland to be as attractive as possible, so he wants to maximize the total area of ​​m pieces of paper in the garland. Calculate what the maximum total area of ​​the pieces of paper in the garland Vasya can get.


-----Input-----

The first line contains a non-empty sequence of n (1 ≤ n ≤ 1000) small English letters ("a"..."z"). Each letter means that Vasya has a sheet of paper of the corresponding color.

The second line contains a non-empty sequence of m (1 ≤ m ≤ 1000) small English letters that correspond to the colors of the pieces of paper in the garland that Vasya wants to make.


-----Output-----

Print an integer that is the maximum possible total area of the pieces of paper in the garland Vasya wants to get or -1, if it is impossible to make the garland from the sheets he's got. It is guaranteed that the answer is always an integer.


-----Examples-----
Input
aaabbac
aabbccac

Output
6

Input
a
z

Output
-1


-----Note-----

In the first test sample Vasya can make an garland of area 6: he can use both sheets of color b, three (but not four) sheets of color a and cut a single sheet of color c in three, for example, equal pieces. Vasya can use the resulting pieces to make a garland of area 6.

In the second test sample Vasya cannot make a garland at all — he doesn't have a sheet of color z.
"""

def calculate_max_garland_area(sheets, garland):
    # Count the occurrences of each color in the sheets and the garland
    cnt_sheets = {}
    cnt_garland = {}
    
    for color in sheets:
        if color not in cnt_sheets:
            cnt_sheets[color] = 0
        cnt_sheets[color] += 1
    
    for color in garland:
        if color not in cnt_garland:
            cnt_garland[color] = 0
        cnt_garland[color] += 1
    
    # Calculate the maximum possible total area
    total_area = 0
    for color in cnt_garland:
        if color not in cnt_sheets:
            return -1  # If a color in the garland is not in the sheets, return -1
        total_area += min(cnt_sheets[color], cnt_garland[color])
    
    return total_area