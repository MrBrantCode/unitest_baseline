"""
QUESTION:
Write a function named `starts_one_ends_correct` that takes one argument `n` and returns the number of n-digit positive integers that either commence or conclude with 1 and are divisible by 2, 3, or 5. Exclude those divisible by multiples of both 3 and 5 but include numbers divisible by 15.
"""

def starts_one_ends_correct(n):
    if n < 1:
        return 0  

    count = 0
    for i in range(10**(n-1), 10**n):  
        str_i = str(i)
        if str_i[0] != '1' and str_i[-1] != '1':
            continue  
        
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            if (i % 3 == 0 and i % 5 == 0 and i % 15 != 0):
                continue
            else:
                count += 1
    return count