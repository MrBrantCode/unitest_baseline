"""
QUESTION:
One day Alex was creating a contest about his friends, but accidentally deleted it. Fortunately, all the problems were saved, but now he needs to find them among other problems.

But there are too many problems, to do it manually. Alex asks you to write a program, which will determine if a problem is from this contest by its name.

It is known, that problem is from this contest if and only if its name contains one of Alex's friends' name exactly once. His friends' names are "Danil", "Olya", "Slava", "Ann" and "Nikita".

Names are case sensitive.


-----Input-----

The only line contains string from lowercase and uppercase letters and "_" symbols of length, not more than 100 — the name of the problem.


-----Output-----

Print "YES", if problem is from this contest, and "NO" otherwise.


-----Examples-----
Input
Alex_and_broken_contest

Output
NO
Input
NikitaAndString

Output
YES
Input
Danil_and_Olya

Output
NO
"""

def is_contest_problem(problem_name: str) -> str:
    friends_names = ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']
    count = 0
    
    for friend in friends_names:
        count += problem_name.count(friend)
    
    if count == 1:
        return "YES"
    else:
        return "NO"