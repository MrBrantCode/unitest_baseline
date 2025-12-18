"""
QUESTION:
Petya works as a PR manager for a successful Berland company BerSoft. He needs to prepare a presentation on the company income growth since 2001 (the year of its founding) till now. Petya knows that in 2001 the company income amounted to a1 billion bourles, in 2002 — to a2 billion, ..., and in the current (2000 + n)-th year — an billion bourles. On the base of the information Petya decided to show in his presentation the linear progress history which is in his opinion perfect. According to a graph Petya has already made, in the first year BerSoft company income must amount to 1 billion bourles, in the second year — 2 billion bourles etc., each following year the income increases by 1 billion bourles. Unfortunately, the real numbers are different from the perfect ones. Among the numbers ai can even occur negative ones that are a sign of the company’s losses in some years. That is why Petya wants to ignore some data, in other words, cross some numbers ai from the sequence and leave only some subsequence that has perfect growth.

Thus Petya has to choose a sequence of years y1, y2, ..., yk,so that in the year y1 the company income amounted to 1 billion bourles, in the year y2 — 2 billion bourles etc., in accordance with the perfect growth dynamics. Help him to choose the longest such sequence.

Input

The first line contains an integer n (1 ≤ n ≤ 100). The next line contains n integers ai ( - 100 ≤ ai ≤ 100). The number ai determines the income of BerSoft company in the (2000 + i)-th year. The numbers in the line are separated by spaces.

Output

Output k — the maximum possible length of a perfect sequence. In the next line output the sequence of years y1, y2, ..., yk. Separate the numbers by spaces. If the answer is not unique, output any. If no solution exist, output one number 0.

Examples

Input

10
-2 1 1 3 2 3 4 -10 -2 5


Output

5
2002 2005 2006 2007 2010


Input

3
-1 -2 -3


Output

0
"""

def find_longest_perfect_sequence(n, income_list):
    # Initialize variables
    years = []
    max_length = 0
    perfect_sequence = []
    
    # Check if the first year (income 1) is in the list
    if 1 in income_list:
        years.append(income_list.index(1))
        i = 2
        while i in income_list[years[-1]:]:
            years.append(income_list[years[-1]:].index(i) + years[-1] + 1)
            i += 1
        
        # Calculate the maximum length and the perfect sequence
        max_length = len(years)
        perfect_sequence = [2001 + year for year in years]
    
    return max_length, perfect_sequence