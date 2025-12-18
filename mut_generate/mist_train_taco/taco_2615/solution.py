"""
QUESTION:
You are given two lists of non-zero digits.

Let's call an integer pretty if its (base 10) representation has at least one digit from the first list and at least one digit from the second list. What is the smallest positive pretty integer?


-----Input-----

The first line contains two integers n and m (1 ≤ n, m ≤ 9) — the lengths of the first and the second lists, respectively.

The second line contains n distinct digits a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 9) — the elements of the first list.

The third line contains m distinct digits b_1, b_2, ..., b_{m} (1 ≤ b_{i} ≤ 9) — the elements of the second list.


-----Output-----

Print the smallest pretty integer.


-----Examples-----
Input
2 3
4 2
5 7 6

Output
25

Input
8 8
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1

Output
1



-----Note-----

In the first example 25, 46, 24567 are pretty, as well as many other integers. The smallest among them is 25. 42 and 24 are not pretty because they don't have digits from the second list.

In the second example all integers that have at least one digit different from 9 are pretty. It's obvious that the smallest among them is 1, because it's the smallest positive integer.
"""

def find_smallest_pretty_integer(list1, list2):
    # Find common digits between list1 and list2
    common_digits = [digit for digit in list1 if digit in list2]
    
    if common_digits:
        # If there are common digits, return the smallest one
        return min(common_digits)
    else:
        # If no common digits, find the smallest digit in each list
        min_list1 = min(list1)
        min_list2 = min(list2)
        
        # Form the smallest pretty integer by concatenating the smallest digits
        if min_list1 < min_list2:
            return int(f"{min_list1}{min_list2}")
        else:
            return int(f"{min_list2}{min_list1}")