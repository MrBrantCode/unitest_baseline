"""
QUESTION:
Write a query to select the first 3 characters of every row from a column called 'name' from a PostgreSQL table. The query should exclude any rows where the first character is a vowel (a, e, i, o, u) and the second character is a digit (0-9).
"""

def filter_names(names):
    vowels = set('aeiou')
    digits = set('0123456789')

    return [name[:3] for name in names 
            if name[0].lower() not in vowels 
            and name[1] not in digits]