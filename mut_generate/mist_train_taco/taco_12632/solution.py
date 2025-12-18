"""
QUESTION:
Revised

The current era, Heisei, will end on April 30, 2019, and a new era will begin the next day. The day after the last day of Heisei will be May 1, the first year of the new era.

In the system developed by the ACM-ICPC OB / OG Association (Japanese Alumni Group; JAG), the date uses the Japanese calendar (the Japanese calendar that expresses the year by the era name and the number of years following it). It is saved in the database in the format of "d days". Since this storage format cannot be changed, JAG saves the date expressed in the Japanese calendar in the database assuming that the era name does not change, and converts the date to the format using the correct era name at the time of output. It was to be.

Your job is to write a program that converts the dates stored in the JAG database to dates using the Heisei or new era. Since the new era has not been announced yet, we will use "?" To represent it.

Input

The input consists of multiple datasets. Each dataset is represented in the following format.

> g y m d

g is a character string representing the era name, and g = HEISEI holds. y, m, and d are integers that represent the year, month, and day, respectively. 1 ≤ y ≤ 100, 1 ≤ m ≤ 12, 1 ≤ d ≤ 31 holds.

Dates that do not exist in the Japanese calendar, such as February 30, are not given as a dataset. When converted correctly as the Japanese calendar, the date on which the era before Heisei must be used is not given as a data set.

The end of the input is represented by a line consisting of only one'#'. The number of datasets does not exceed 100.

Output

For each data set, separate the converted era, year, month, and day with a space and output it on one line. If the converted era is "Heisei", use "HEISEI" as the era, and if it is a new era, use "?".

Normally, the first year of the era is written as the first year, but in the output of this problem, ignore this rule and output 1 as the year.

Sample Input


HEISEI 1 1 8
HEISEI 31 4 30
HEISEI 31 5 1
HEISEI 99 12 31
HEISEI 38 8 30
HEISEI 98 2 22
HEISEI 2 3 26
HEISEI 28 4 23



Output for the Sample Input


HEISEI 1 1 8
HEISEI 31 4 30
? 1 5 1
? 69 12 31
? 8 8 30
? 68 2 22
HEISEI 2 3 26
HEISEI 28 4 23






Example

Input

HEISEI 1 1 8
HEISEI 31 4 30
HEISEI 31 5 1
HEISEI 99 12 31
HEISEI 38 8 30
HEISEI 98 2 22
HEISEI 2 3 26
HEISEI 28 4 23
#


Output

HEISEI 1 1 8
HEISEI 31 4 30
? 1 5 1
? 69 12 31
? 8 8 30
? 68 2 22
HEISEI 2 3 26
HEISEI 28 4 23
"""

def convert_japanese_date(g, y, m, d):
    """
    Converts a date from the Heisei era to the correct era (Heisei or new era).

    Parameters:
    g (str): The era name, which is always "HEISEI" for this problem.
    y (int): The year in the Heisei era.
    m (int): The month.
    d (int): The day.

    Returns:
    tuple: A tuple containing the converted era name, year, month, and day.
           The era name will be "HEISEI" if the date is within the Heisei era,
           or "?" if the date is in the new era.
    """
    y = int(y)
    m = int(m)
    d = int(d)
    
    if y == 31 and m >= 5:
        return ('?', 1, m, d)
    elif y >= 32:
        return ('?', y - 30, m, d)
    else:
        return (g, y, m, d)