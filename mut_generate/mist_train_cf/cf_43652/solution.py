"""
QUESTION:
Write a function `oddNumberStats` that takes a list of positive integers less than 100 as input. The function should return a tuple containing the sum of all odd numbers in the list, the count of odd numbers, and a dictionary where the keys represent ranges (1-10, 11-20, etc.) and the values represent the count of odd numbers in each range.
"""

def oddNumberStats(arr):
    sum_odd = 0
    count = 0
    bins_dict = {f"{10 * i + 1}-{10 * (i + 1)}": 0 for i in range(10)}
    for num in arr:
        if num % 2 != 0:
            sum_odd += num
            count += 1
            bins_key = f"{num//10*10 + 1}-{(num//10 + 1)*10}"
            bins_dict[bins_key] += 1
    return sum_odd, count, bins_dict