"""
QUESTION:
Given two lists A and B containing jumbled integers, where A should only have odd numbers and B should only have even numbers, write a function `find_error_and_missing(A, B, lower, upper)` that identifies the misplaced elements in each list, corrects the lists, and finds the missing numbers in each list within the range from `lower` to `upper`. The function should return a dictionary with the corrected and misplaced elements in A and B, as well as the missing elements from each list.
"""

def find_error_and_missing(A, B, lower, upper):
    correct_A, correct_B = [], []   # Correct lists.
    wrong_A, wrong_B = [], []   # Lists with wrong numbers.

    for num in A:
        if num % 2 != 0:
            correct_A.append(num)
        else:
            wrong_A.append(num)

    for num in B:
        if num % 2 == 0:
            correct_B.append(num)
        else:
            wrong_B.append(num)

    missing_A = [i for i in range(lower, upper + 1, 2) if i not in correct_A]   # Finding missing odd numbers.
    missing_B = [i for i in range(lower + 1, upper + 1, 2) if i not in correct_B]   # Finding missing even numbers.

    return {"A": {"Correct": correct_A, "Wrong": wrong_A, "Missing": missing_A},
            "B": {"Correct": correct_B, "Wrong": wrong_B, "Missing": missing_B}}