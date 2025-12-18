"""
QUESTION:
Write a function `sort_statements` that takes a list of strings as input, where each string is a statement containing only lowercase letters and has a maximum length of 100 characters. The function should return the sorted list of statements in ascending order based on the number of vowels in each statement. If two or more statements have the same number of vowels, they should be sorted in descending order based on the length of each statement. If two or more statements have the same number of vowels and length, they should be sorted alphabetically.
"""

def sort_statements(statements):
    def count_vowels(statement):
        return sum(1 for char in statement if char in 'aeiou')

    return sorted(statements, key=lambda statement: (count_vowels(statement), -len(statement), statement))