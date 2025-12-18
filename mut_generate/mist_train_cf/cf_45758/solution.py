"""
QUESTION:
Given a list of strings with numerical characters, write a function `unusual_addition` that returns a list where each string is replaced with a new string with the count of odd numbers in the original string and the sum of these odd numbers. The new string should replace every occurrence of 'i' with the count of odd numbers and include the string position in the original list, and append the sum of odd numbers as a separate element in the output list.
"""

def unusual_addition(lst):
    out = []
    for i in range(len(lst)):
        current_str = lst[i]
        num_odds = 0
        sum_odds = 0
        for ch in current_str:
            if int(ch) % 2 != 0:
                num_odds += 1
                sum_odds += int(ch)

        out.append(f"the number of odd elements {num_odds}n the str{num_odds}ng {i + 1} of the {num_odds}nput.")
        out.append(sum_odds)
    
    return out