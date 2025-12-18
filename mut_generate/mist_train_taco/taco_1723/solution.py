"""
QUESTION:
The king Copa often has been reported about the Codeforces site, which is rapidly getting more and more popular among the brightest minds of the humanity, who are using it for training and competing. Recently Copa understood that to conquer the world he needs to organize the world Codeforces tournament. He hopes that after it the brightest minds will become his subordinates, and the toughest part of conquering the world will be completed.

The final round of the Codeforces World Finals 20YY is scheduled for DD.MM.YY, where DD is the day of the round, MM is the month and YY are the last two digits of the year. Bob is lucky to be the first finalist form Berland. But there is one problem: according to the rules of the competition, all participants must be at least 18 years old at the moment of the finals. Bob was born on BD.BM.BY. This date is recorded in his passport, the copy of which he has already mailed to the organizers. But Bob learned that in different countries the way, in which the dates are written, differs. For example, in the US the month is written first, then the day and finally the year. Bob wonders if it is possible to rearrange the numbers in his date of birth so that he will be at least 18 years old on the day DD.MM.YY. He can always tell that in his motherland dates are written differently. Help him.

According to another strange rule, eligible participant must be born in the same century as the date of the finals. If the day of the finals is participant's 18-th birthday, he is allowed to participate. 

As we are considering only the years from 2001 to 2099 for the year of the finals, use the following rule: the year is leap if it's number is divisible by four.

Input

The first line contains the date DD.MM.YY, the second line contains the date BD.BM.BY. It is guaranteed that both dates are correct, and YY and BY are always in [01;99].

It could be that by passport Bob was born after the finals. In this case, he can still change the order of numbers in date.

Output

If it is possible to rearrange the numbers in the date of birth so that Bob will be at least 18 years old on the DD.MM.YY, output YES. In the other case, output NO. 

Each number contains exactly two digits and stands for day, month or year in a date. Note that it is permitted to rearrange only numbers, not digits.

Examples

Input

01.01.98
01.01.80


Output

YES


Input

20.10.20
10.02.30


Output

NO


Input

28.02.74
28.02.64


Output

NO
"""

from itertools import permutations

def is_eligible_to_participate(final_date: str, birth_date: str) -> bool:
    # Helper function to check if a year is leap
    def is_leap_year(year: int) -> bool:
        return year % 4 == 0
    
    # Helper function to check if a date is valid
    def is_valid_date(day: int, month: int, year: int) -> bool:
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        if month == 2:
            if is_leap_year(year):
                return day <= 29
            else:
                return day <= 28
        else:
            return day <= [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
    
    # Parse the final date
    final_day, final_month, final_year = map(int, final_date.split('.'))
    
    # Parse the birth date
    birth_day, birth_month, birth_year = map(int, birth_date.split('.'))
    
    # Check all permutations of the birth date
    for day, month, year in permutations([birth_day, birth_month, birth_year]):
        if is_valid_date(day, month, year):
            # Check if the participant is at least 18 years old
            if final_year - year > 18 or (final_year - year == 18 and (final_month > month or (final_month == month and final_day >= day))):
                return True
    return False