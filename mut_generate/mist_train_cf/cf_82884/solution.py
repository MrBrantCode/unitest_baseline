"""
QUESTION:
Write a function named `five_div_seq` that takes an integer `n` and returns the total count of digit 5 in integers less than `n` that are divisible by 9 or 14, and are part of a decreasing arithmetic sequence with an even common difference containing at least three elements.
"""

def five_div_seq(n: int) -> int:
    num_list = [i for i in range(n - 1, 0, -1) if i % 9 == 0 or i % 14 == 0]
    num_5_count = 0
    
    for i in range(len(num_list) - 2):
        if (num_list[i] - num_list[i+1]) % 2 == 0 and (num_list[i+1] - num_list[i+2]) % 2 == 0 and (num_list[i] - num_list[i+1]) == (num_list[i+1] - num_list[i+2]):
            num_5_count += str(num_list[i]).count('5')
            num_5_count += str(num_list[i+1]).count('5')
            num_5_count += str(num_list[i+2]).count('5')

    return num_5_count