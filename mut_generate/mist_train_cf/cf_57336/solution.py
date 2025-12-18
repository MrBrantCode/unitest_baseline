"""
QUESTION:
Create a function called `starts_one_ends` that takes a positive integer `n` as input and returns the count of n-digit positive numbers that start or end with 1, are divisible by 3 or 5, but not both, and have at most one '1' in every chunk of 3 consecutive digits. The function should iterate over all n-digit numbers and check these conditions.
"""

def starts_one_ends(n):
    tally = 0
    for i in range(10 ** (n - 1), 10 ** n):
        str_i = str(i)
        if str_i[0] == '1' or str_i[-1] == '1':  
            if i % 15 != 0 and (i % 3 == 0 or i % 5 == 0):  
                chunks = [str_i[j:j+3] for j in range(0, len(str_i), 3)]  
                if all(chunk.count('1') <= 1 for chunk in chunks):  
                    tally += 1
    return tally