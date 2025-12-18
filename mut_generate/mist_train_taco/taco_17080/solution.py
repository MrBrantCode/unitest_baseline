"""
QUESTION:
Problem

One day, Kawabayashi is about to have lunch at the school cafeteria. There are three types of daily lunch menus for school cafeterias: A lunch, B lunch, and C lunch.
Kawabayashi is a glutton, so I would like to eat all three types of daily lunch menus one by one.
However, Kawabayashi decided to put up with one type of lunch menu and eat two different types of lunch menus so as to minimize the total calorie intake with care for his health.
Ask for a lunch menu that Kawabayashi will endure when given the calories of A, B, and C lunches one day.

Constraints

The input satisfies the following conditions.

* $ 1 \ leq a, b, c \ leq 5000 $
* $ a \ neq b, b \ neq c, c \ neq a $

Input

The input is given in the following format.


$ a $ $ b $ $ c $


Three integers $ a $, $ b $, $ c $ are given, separated by spaces. Each represents the calories of A lunch, B lunch, and C lunch one day.

Output

Output the menu name that Kawabayashi will endure on one line.
"A" to put up with A lunch
"B" to put up with B lunch
"C" to put up with C lunch
Output.

Examples

Input

1000 900 850


Output

A


Input

1000 800 1200


Output

C
"""

def determine_endured_menu(a: int, b: int, c: int) -> str:
    if a > b and a > c:
        return 'A'
    elif b > a and b > c:
        return 'B'
    else:
        return 'C'