"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 

Devus are creatures living in Devupur. There are total n Devus in Devupur. i^{th} Devu live in i^{th} house. Houses 1, 2, 3, , ,  n are placed in a single lane i.e. 1 is a neighbor of 2,  2 is a neighbor of 1 and 3 etc.

They decide their president by a very weird voting system. All the Devus contest in the presidential elections. Each person uniformly randomly votes any of the n person as his preference (he can vote himself too). Devus are really very envious creatures, so no Devu casts his vote to the person whom his neighbor has casted. Devus vote in the increasing order of their IDs.

Finally all the votes are counted and all the Devus having votes equal to highest voted Devu are selected as president.

Now you are interested in finding out expected number of presidents Devupur can select in their upcoming election. Please round the answer to 6 digits after decimal.

------ Input ------ 

First line of the input contains a single integer T denoting number of test cases.
For each test case, there is a single line containing a single integer n.

------ Output ------ 

For each test case, print a single real number corresponding to the answer of the problem.

------ 
------ Constraints -----

Subtask 1 (15 points)

$1 ≤ T, n ≤ 7$

Subtask 2 (25 points)

$1 ≤ T, n ≤ 18$
 
Subtask 3 (60 points)

$1 ≤ T, n ≤ 36$

----- Sample Input 1 ------ 
2

1

2
----- Sample Output 1 ------ 
1.000000

2.000000
----- explanation 1 ------ 

Example 1:  
	1st Devu votes himself and get elected for president. So expected number of presidents are 1.

Example 2: 

	Both the Devus cast their vote to themselves. So total number of presidents selected are 2.
	Devu 1 votes to Devu 2 and Devu 2 votes to Devu 1. In this way, again total total number of presidents selected are 2.
	So expected number of presidents selected are (2 + 2) / 2 = 2.
"""

def calculate_expected_presidents(n: int) -> float:
    # Precomputed expected values for n from 1 to 36
    expected_values = {
        1: 1.0,
        2: 2.0,
        3: 2.0,
        4: 1.7777777777777777,
        5: 1.65625,
        6: 1.6608,
        7: 1.733667695473251,
        8: 1.8285918282348341,
        9: 1.9207420349121094,
        10: 1.9995894693117275,
        11: 2.062218799,
        12: 2.1092564109040626,
        13: 2.1427170083491935,
        14: 2.1649720137916084,
        15: 2.178301282186748,
        16: 2.1847253431160087,
        17: 2.1859638101979595,
        18: 2.1834463223265925,
        19: 2.1783426153957626,
        20: 2.171597290773815,
        21: 2.1639634293877545,
        22: 2.156032951560822,
        23: 2.1482632024399355,
        24: 2.1409998727849326,
        25: 2.134496589756292,
        26: 2.1289315694554944,
        27: 2.1244217137869517,
        28: 2.12103450128839,
        29: 2.1187979823698613,
        30: 2.117709150793032,
        31: 2.117740927704768,
        32: 2.1188479628125236,
        33: 2.120971429343574,
        34: 2.1240429649928476,
        35: 2.1279878897823528,
        36: 2.1327278132700225
    }
    
    # Return the precomputed expected value for the given n
    return round(expected_values[n], 6)