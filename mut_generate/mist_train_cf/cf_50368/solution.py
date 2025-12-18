"""
QUESTION:
Write a function even_odd_count that takes an integer as input and returns two lists. The first list contains the counts of consecutive sequences of even digits and the second list contains the counts of consecutive sequences of odd digits in the input integer, treating negative numbers as positive.
"""

def entance(num):
    num = str(abs(num))  # Convert to string and remove negative sign if present
    even_count, odd_count = [], []
    i = 0
    while i < len(num):
        count = 1
        while i + 1 < len(num) and num[i] == num[i + 1]:
            i += 1
            count += 1
        if int(num[i]) % 2 == 0:
            even_count.append(count)
        else:
            odd_count.append(count)
        i += 1
    return even_count, odd_count