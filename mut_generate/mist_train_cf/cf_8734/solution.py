"""
QUESTION:
Write a function named `divide_list` that takes a list of even number of integers as input and returns two halves of the list. The two halves should have the same sum of elements. If it is not possible to divide the list into two halves with equal sums, return a message "Cannot divide list into two equal halves with equal sums".
"""

def divide_list(lst):
    total_sum = sum(lst)
    if total_sum % 2 != 0:
        return "Cannot divide list into two equal halves with equal sums"

    target_sum = total_sum // 2
    current_sum = 0
    first_half = []
    second_half = []

    for num in lst:
        if current_sum + num <= target_sum:
            first_half.append(num)
            current_sum += num
        else:
            second_half.append(num)

    if sum(first_half) != target_sum:
        return "Cannot divide list into two equal halves with equal sums"

    return first_half, second_half