"""
QUESTION:
Write a function `five_div_seq(n: int)` that calculates the frequency of the digit 5 in integers less than n, where these numbers are divisible by either 9 or 14 and form a decremental arithmetic sequence with an even difference, and include at least 3 elements in the sequence.
"""

def five_div_seq(n: int):
    num_list = []

    # Find all numbers less than n divisible by 9 or 14
    for i in range(n-1, 0, -1):
        if i % 9 == 0 or i % 14 == 0:
            num_list.append(i)

        if len(num_list) >= 3 and num_list[-1] - num_list[-2] == num_list[-2] - num_list[-3]:
            break

    # Count the number of times '5' appears in the numbers
    count = 0
    for num in num_list:
        count += str(num).count('5')

    return count