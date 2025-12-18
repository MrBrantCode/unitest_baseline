"""
QUESTION:
A recently found Ancient Prophesy is believed to contain the exact Apocalypse date. The prophesy is a string that only consists of digits and characters "-".

We'll say that some date is mentioned in the Prophesy if there is a substring in the Prophesy that is the date's record in the format "dd-mm-yyyy". We'll say that the number of the date's occurrences is the number of such substrings in the Prophesy. For example, the Prophesy "0012-10-2012-10-2012" mentions date 12-10-2012 twice (first time as "0012-10-2012-10-2012", second time as "0012-10-2012-10-2012").

The date of the Apocalypse is such correct date that the number of times it is mentioned in the Prophesy is strictly larger than that of any other correct date.

A date is correct if the year lies in the range from 2013 to 2015, the month is from 1 to 12, and the number of the day is strictly more than a zero and doesn't exceed the number of days in the current month. Note that a date is written in the format "dd-mm-yyyy", that means that leading zeroes may be added to the numbers of the months or days if needed. In other words, date "1-1-2013" isn't recorded in the format "dd-mm-yyyy", and date "01-01-2013" is recorded in it.

Notice, that any year between 2013 and 2015 is not a leap year.

Input

The first line contains the Prophesy: a non-empty string that only consists of digits and characters "-". The length of the Prophesy doesn't exceed 105 characters.

Output

In a single line print the date of the Apocalypse. It is guaranteed that such date exists and is unique.

Examples

Input

777-444---21-12-2013-12-2013-12-2013---444-777


Output

13-12-2013
"""

def find_apocalypse_date(prophesy: str) -> str:
    n = len(prophesy)
    l = list('0987654321')
    cnt = {}
    
    for i in range(n - 9):
        t = prophesy[i:i + 10]
        if (t[0] in l and t[1] in l and t[2] == '-' and
            t[3] in l and t[4] in l and t[5] == '-' and
            t[6] in l and t[7] in l and t[8] in l and t[9] in l):
            year = int(t[6:10])
            month = int(t[3:5])
            day = int(t[0:2])
            
            if 2013 <= year <= 2015 and 1 <= month <= 12:
                if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
                    cnt[t] = cnt.get(t, 0) + 1
                elif month in [4, 6, 9, 11] and 1 <= day <= 30:
                    cnt[t] = cnt.get(t, 0) + 1
                elif month == 2 and 1 <= day <= 28:
                    cnt[t] = cnt.get(t, 0) + 1
    
    return max(cnt, key=cnt.get)