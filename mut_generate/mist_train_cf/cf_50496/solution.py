"""
QUESTION:
Write a function named `five_div_seq` that calculates the frequency of the digit '5' in numbers less than 'n'. These numbers should be divisible by 9 or 14, have at least three digits, and form a decreasing arithmetic sequence with an even common difference. The function should take one integer argument 'n' and return the frequency of '5'.
"""

def five_div_seq(n): 
    digit = '5'
    seq = []

    # condition: numbers less than 'n', divisible by either 9 or 14, have at least three digits
    for num in range(min(n, 1000), 100, -18):  
        if num % 9 == 0 or num % 14 == 0:
            if digit in str(num):
                seq.append(num)

    # from this point we already have a descending sequence with common difference 18

    # count number of occurrences of '5'
    result = sum(s.count(digit) for s in map(str, seq))

    return result